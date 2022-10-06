import serial,json,time,os
import argparse,re

OUTPATH = "devices"
REGEX = re.compile(r"\[(\w+)\.(?:(\d+)\.)?(\w+)([?!=]?)(?:(\d+))?(?:\?(\d+))?\|(.+)\]",re.DOTALL)
GRP_CLS         = 0
GRP_INSTANCE    = 1
GRP_CMD         = 2
GRP_TYPE        = 3
GRP_CMDVAL1     = 4
GRP_CMDVAL2     = 5
GRP_REPLY       = 6

class CommandHelpReader:
    def __init__(self,port):
        self.port = port
        self.open()
        self.dev.timeout = 1
        self.devicename = self.sendCommand("sys.hwtype?")
        self.already_read = set()

    def __del__(self):
        self.dev.close()

    def removeEntry(self,entry):
        self.already_read.remove(entry)
    def close(self):
        self.dev.close()

    def open(self):
        self.dev = serial.Serial(self.port,115200)

    def sendCommand(self,cmd):
        self.dev.write(bytes(cmd+';','utf-8'))
        #time.sleep(1)
        reply = (self.dev.read_until(b']')).decode('utf-8')
        
        match = REGEX.search(reply)
        if not match:
            return None
        groups = match.groups()
        cmd = groups[GRP_CMD]
        reply = str(groups[GRP_REPLY])
        return reply



    def listToMd(self,list,makeHeader=True):
        def mdLine(line,spacer=False): # Makes a markdown line with spacer from a list of strings
            l = '|'+'|'.join(line)+'|'
            s = ""
            if spacer:
                s += "\n|"
                for t in line:
                    s += '-' * len(t) + '|'
            return l+s+'\n'
    
        out = ""
        start = 0
        if makeHeader:
            # Use first line as header
            start = 1
            out = mdLine(list[0],True)

        for line in list[start::]:
            out += mdLine(line)

        return out

    def getHelp(self,cls,instance=0,writefile=True,noduplicates = True):
        cmd = f"{cls}.{instance}.help!"
        reply = self.sendCommand(cmd)
        
        if not reply or (cls in self.already_read and noduplicates):
            #print("Skipping",cls)
            return ""

        lines = [line.split(',') for line in reply.splitlines() if line]

        classname = self.sendCommand(f"{cls}.name")
        classname_long = lines[1][2]
        if not classname:
            classname = classname_long

        # Save raw csv into file
        if writefile:
            filepath = os.path.join(OUTPATH,self.devicename)
            os.makedirs(filepath,exist_ok=True)
            with open(os.path.join(filepath,f"{classname}.txt"),"w") as f:
                f.write(reply)

        # format into list
        print(f"Help: {classname}")
        
        helpentry = f"\n### {classname}\n\n"
        helpentry += self.listToMd(lines[0:2]) # first 2 lines are classinfo
        helpentry += '\n'
        helpentry += self.listToMd(lines[2::])
        helpentry += '\n---\n'
        self.already_read.add(cls)
        return helpentry

    def getAllActiveHelp(self):
        """"Gets help of all not already read active classes"""
        helpentry = ""
        active = self.sendCommand("sys.lsactive?")
        for line in active.split("\n"):
            linelist = line.split(":")
            cls = linelist[1]
            helpentry += self.getHelp(cls,noduplicates=True)

        return helpentry



        
        
def enableButtons(reader : CommandHelpReader):
    # Button sources
    types = [b.split(":") for b in reader.sendCommand("main.lsbtn?").split("\n")]

    commands_markdown = "### Button sources\n"
    for t in types:
        name = t[2]
        commands_markdown += f"- {name}\n"

    # Enable all button types
    b = 0
    for t in types:
        b |= (1 << int(t[0]))

    reader.sendCommand(f"main.btntypes={b}")
    return commands_markdown

def enableAnalog(reader : CommandHelpReader):
    # analog sources
    types = [b.split(":") for b in reader.sendCommand("main.lsain?").split("\n")]
    # Enable all analog types
    b = 0
    for t in types:
        b |= (1 << int(t[0]))

    reader.sendCommand(f"main.aintypes={b}")

def readEnctypes(reader : CommandHelpReader):
    types = [b.split(":") for b in reader.sendCommand("axis.enctype!").split("\n")]
    commands_markdown = "### Encoders\n"
    for t in types:
        name = t[2]
        commands_markdown += f"- {name}\n"

    commands_markdown += "---\n"
    for t in types:
        if t[0] == "0": 
            continue
        reader.sendCommand("axis.enctype=0") # Reset
        reader.sendCommand(f"axis.enctype={t[0]}")
        commands_markdown += reader.getAllActiveHelp()
    
    return commands_markdown

def readDrivers(reader : CommandHelpReader):
    types = [b.split(":") for b in reader.sendCommand("axis.drvtype!").split("\n")]
    commands_markdown = "### Drivers\n"

    for t in types:
        name = t[2]
        commands_markdown += f"- {name}\n"
    commands_markdown += "---\n"
    for t in types:
        if t[0] == "0": 
            continue
        reader.sendCommand("axis.drvtype=0") # Reset
        reader.sendCommand(f"axis.drvtype={t[0]}")
        commands_markdown += reader.getAllActiveHelp()
    reader.sendCommand("axis.drvtype=0") # Reset

    return commands_markdown

def readMainclasses(reader : CommandHelpReader):
    types = [b.split(":") for b in reader.sendCommand("sys.lsmain?").split("\n")]
    commands_markdown = "### Other mainclasses\n"
    for t in types:
        name = t[2]
        commands_markdown += f"- {name}\n"
    commands_markdown += "---\n"
    for t in types:
        if t[0] == "1": # ffbwheel already read 
            continue
        reader.sendCommand(f"sys.main={t[0]}\n")
        # Disconnect and reconnect
        #time.sleep(1)#wait for write
        reader.close()
        time.sleep(4)#wait for reconnect
        reader.open()
        reader.removeEntry("main")
        commands_markdown += reader.getAllActiveHelp()


    return commands_markdown


def makeCommands(reader : CommandHelpReader):
    commands_markdown = ""
    with open("header.txt","r") as f:
        commands_markdown += f.read() + "\n\n"
    reader.sendCommand("sys.debug=1") # Enable debug mode

    if reader.sendCommand("main?") != '1':
        reader.sendCommand("main=1") # ffbwheel

    reader.sendCommand("axis.enctype=0")
    reader.sendCommand("axis.drvtype=0")

    commands_markdown += reader.getHelp("sys")
    commands_markdown += reader.getHelp("main")
    commands_markdown += reader.getHelp("fx")
    commands_markdown += reader.getHelp("axis")

    commands_markdown += reader.getAllActiveHelp()

    commands_markdown += enableButtons(reader)
    commands_markdown += reader.getAllActiveHelp()
    reader.sendCommand(f"main.btntypes=0")

    enableAnalog(reader)
    commands_markdown += reader.getAllActiveHelp()
    reader.sendCommand(f"main.aintypes=0")

    commands_markdown += readEnctypes(reader)
    commands_markdown += readDrivers(reader)

    # Other mainclasses
    commands_markdown += readMainclasses(reader)

    ver = reader.sendCommand("sys.swver")
    commands_markdown += f"State: v{ver}\n"

    with open("footer.txt","r") as f:
        commands_markdown += f.read()


    with open(os.path.join("..","Commands.md"),"w") as f:
        f.write(commands_markdown)

def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--port",action="store", type=str,help="Serial port for device mode")

    args = parser.parse_args()

    if args.port:
        print("Read mode\n")
        reader = CommandHelpReader(args.port)
        makeCommands(reader)

    


if __name__ == "__main__":
    main()