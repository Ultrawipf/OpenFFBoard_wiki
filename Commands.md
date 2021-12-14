## Commands:
Valid from version 1.5 on.
### Syntax for string based Interfaces. (CDC and UART):
#### Request format:
Get: `cls.(instance.)cmd?` or `cls.(instance.)cmd?adr`

Set: `cls.(instance.)cmd=val` or `cls.(instance.)cmd=val?adr`

Info `cls.(instance.)cmd!` sometimes used for generating a list of supported options. Check source code for mode info.

Values can be supplied as hex (`x4d2`) or base 10 (`1234`). 

Commands with 2 values are rarely used. One example is setting a register in the TMC or passing a CAN frame with a target address and value.

#### Reply format:
`[cls.instance.cmd?|val]` or `[cls.instance.cmd?|adr,val]` for get commands

`[cls.instance.cmd=val|OK]` or `[cls.instance.cmd=val?adr|OK]`  for set commands

Some commands return strings in a custom format (Like help commands) and do not work with the HID command system.

### Syntax for HID:
Structure for the vendor defined reports:

report ID: 0xA1
type(0x01 8b): `{write = 0, request = 1, info = 2, writeAddr = 3, requestAddr = 4,ACK = 10, notFound = 13, notification = 14, err = 15}`
use write or request or info depending on the command. Write will SET an internal field to the value (Like the `=val` commands).

For commands that accept 2 values use writeAddr and supply value and address.
The lsactive command will report a list of active classes.

- classID(0x02 16b): id of the targeted class. 0 = system, 1 = main... 
- instance(0x03 8b): instance of the targeted class. Often 0 but for example there can be multiple axes or drivers.
- cmd(0x04 32b): command ID
- data(0x05 64b): the first data value to send
- addr(0x06 64b): the second data value to send

HID commands only work when the HID command interface is active and the according fields present in the HID report.
This is by default the case for the FFB class but not in the failsafe fallback and other non HID classes.

<details>
    <summary>Python example</summary>
    <code class="language-python">

    import pywinusb.hid as hid
    import time
    import struct

    # Receive and print data
    def readData(data):
        if(data[0] == 0xA1):
            t = data[1]
            cls = struct.unpack('<H', bytes(data[2:4]))
            instance = data[4]
            cmd = struct.unpack('<L', bytes(data[5:9]))
            val = struct.unpack('<Q', bytes(data[9:17]))
            addr = struct.unpack('<Q', bytes(data[17:25]))
            print(f"Type: {t}, Class: {cls}.{instance}: cmd: {cmd}, val: {val}, addr: {addr}")


    def sendCommand(report,type,cls,inst,cmd,data=0,adr=0):
        report[hid.get_full_usage_id(0xff00, 0x01)]=type # type. (0 = write, 1 = read)
        report[hid.get_full_usage_id(0xff00, 0x02)]=cls # cls (axis)
        report[hid.get_full_usage_id(0xff00, 0x03)]=inst # instance
        report[hid.get_full_usage_id(0xff00, 0x04)]=cmd # cmd (power)
        report[hid.get_full_usage_id(0xff00, 0x05)]=data # data
        report[hid.get_full_usage_id(0xff00, 0x06)]=adr # adr
        report.send()

    def main():
        device = hid.HidDeviceFilter(vendor_id = 0x1209,product_id = 0xFFB0).get_devices()[0]
        device.open()

        device.set_raw_data_handler(readData)

        reports = device.find_output_reports(0xff00,0x01)
        if(reports):
            report = reports[0]
            print("Found",report)
            sendCommand(report,1,0xA01,0,0x00,0) # get power
            sendCommand(report,0,0xA01,0,0x00,1337) # set power
            sendCommand(report,1,0xA01,0,0x00,0) # get power

        while device.is_plugged():
            time.sleep(0.5)
        device.close()

    if __name__ == '__main__':
        main()
</code></details>


## Command list


### System commands
|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|sys.0 |0x0                          |System Commands                                          |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|help  |0x0                          |Print system help                                        |
|save  |0x1                          |Write all settings to flash                              |
|reboot|0x2                          |Reset chip                                               |
|dfu   |0x3                          |reboot into DFU bootloader                               |
|lsmain|0x6                          |List available mainclasses                               |
|lsactive|0x8                          |List active classes                                      |
|vint  |0xE                          |Internal voltage                                         |
|vext  |0xF                          |External voltage                                         |
|main  |0x7                          |Query or change mainclass                                |
|swver |0x4                          |Firmware version                                         |
|hwtype|0x5                          |Hardware type                                            |
|flashraw|0xD                          |Write value to flash address                             |
|flashdump|0xC                          |Read all flash variables                                 |
|errors|0xA                          |Read error states                                        |
|errorsclr|0xB                          |Reset errors                                             |
|heapfree|0x11                         |Memory info                                              |
|format|0x9                          |set format=1 to erase all stored values                  |

---

### FFB Wheel
|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|main.0|0x1                          |FFB Wheel: Force feedback HID game controller            |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|axes  |0x1                          |Number of axes (1-2)                                     |
|ffbactive|0x0                          |FFB status                                               |
|btntypes|0x2                          |Enabled button sources                                   |
|addbtn|0x4                          |Enable button source                                     |
|lsbtn |0x3                          |Get available button sources                             |
|aintypes|0x5                          |Enabled analog sources                                   |
|lsain |0x6                          |Get available analog sources                             |
|addain|0x7                          |Enable analog source                                     |
|hidrate|0x8                          |Get estimated effect update speed                        |
|hidsendspd|0x9                          |Change HID gamepad update rate                           |

---

### FFB effects
|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|fx.0  |0xA02                        |Effects: Controls internal FFB effects                   |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|filterCfFreq|0x0                          |Constant force filter frequency                          |
|filterCfQ|0x1                          |Constant force filter Q-factor                           |
|spring|0x3                          |Spring gain                                              |
|friction|0x4                          |Friction gain                                            |
|damper|0x5                          |Damper gain                                              |
|inertia|0x6                          |Inertia gain                                             |
|effects|0x2                          |List effects                                             |

---

### FFB axis

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|axis.0|0xA01                        |Axis: FFB axis                                           |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|power |0x0                          |Overall force strength                                   |
|degrees|0x1                          |Rotation range in deg.                                   |
|esgain|0x2                          |Endstop stiffness                                        |
|zeroenc|0x3                          |Zero axis                                                |
|invert|0x4                          |Invert axis                                              |
|idlespring|0x5                          |Idle spring strength                                     |
|axisdamper|0x6                          |Independent damper effect                                |
|enctype|0x7                          |Encoder type get/set/list                                |
|drvtype|0x8                          |Motor driver type get/set/list                           |
|pos   |0x9                          |Axis position                                            |
|maxspeed|0xA                          |Speed limit in deg/s                                     |
|maxtorquerate|0xB                          |Torque rate limit in counts/ms                           |
|fxratio|0xC                          |Effect ratio. Reduces effects excluding endstop. 255=100%|

---

### MT SPI encoder

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|mtenc.0|0x62                         |MT6825 SPI3                                              |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|cs    |0x0                          |CS pin                                                   |

---

### Digital pin buttons

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|dpin.0|0x21                         |D-Pins: Digital pin button source                        |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|mask  |0x0                          |Enabled pins                                             |
|polarity|0x1                          |Pin polarity                                             |
|pins  |0x2                          |Available pins                                           |

---

### Analog pin axes

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|apin.0|0x41                         |AIN-Pins: Analog pins source                             |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|mask  |0x0                          |Enabled pins                                             |
|autocal|0x1                          |Autoranging                                              |
|pins  |0x2                          |Available pins                                           |


---

### PWM motor driver

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|pwmdrv.0|0x84                         |PWM: PWM output motor driver                             |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|freq  |0x1                          |PWM period selection                                     |
|mode  |0x0                          |PWM mode                                                 |

---

### TMC4671 motor driver

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|tmc.0 |0x81                         |TMC4671: TMC4671 interface                               |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|cpr   |0x0                          |CPR in TMC                                               |
|mtype |0x1                          |Motor type                                               |
|encsrc|0x2                          |Encoder source                                           |
|tmcHwType|0x3                          |Version of TMC board                                     |
|encalign|0x4                          |Align encoder                                            |
|poles |0x5                          |Motor pole pairs                                         |
|acttrq|0x6                          |Read torque                                              |
|pwmlim|0x7                          |PWM limit                                                |
|torqueP|0x8                          |Torque P                                                 |
|torqueI|0x9                          |Torque I                                                 |
|fluxP |0xA                          |Flux P                                                   |
|fluxI |0xB                          |Flux I                                                   |
|velocityP|0xC                          |Velocity P                                               |
|velocityI|0xD                          |Velocity I                                               |
|posP  |0xE                          |Pos P                                                    |
|posI  |0xF                          |Pos I                                                    |
|tmctype|0x10                         |Version of TMC chip                                      |
|pidPrec|0x11                         |PID precision bit0=I bit1=P. 0=Q8.8 1= Q4.12             |
|phiesrc|0x12                         |PhiE source                                              |
|fluxoffset|0x13                         |Offset flux scale for field weakening                    |
|seqpi |0x14                         |Sequential PI                                            |
|iScale|0x15                         |Counts per A                                             |
|encdir|0x16                         |Encoder dir                                              |
|temp  |0x17                         |Temperature in C * 100                                   |
|reg   |0x18                         |Read or write a TMC register at adr                      |

---

### ODrive motor driver (CAN)
Example here is only M0. M1 is available too.

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|odrv.0|0x85                         |ODrive (M0): ODrive motor driver with CAN                |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|canid |0x0                          |CAN id of ODrive                                         |
|canspd|0x1                          |CAN baudrate                                             |
|errors|0x2                          |ODrive error flags                                       |
|state |0x3                          |ODrive state                                             |
|maxtorqe|0x4                          |Max torque to send for scaling                           |
|vbus  |0x5                          |ODrive Vbus                                              |
|anticogging|0x6                          |Set 1 to start anticogging calibration                   |

---

### VESC motor driver

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|vesc.0|0x87                         |VESC: VESC CAN interface                                 |

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|canid |0x0                          |CAN id of VESC                                           |
|canspd|0x1                          |CAN baud (3=250k 4=500k 5=1M)                            |
|errorflags|0x2                          |VESC error state                                         |
|vescstate|0x3                          |VESC state                                               |
|voltage|0x4                          |VESC supply voltage                                      |
|encrate|0x5                          |Encoder update rate                                      |
|pos   |0x6                          |VESC position                                            |
|torque|0x7                          |Current VESC torque                                      |
|forceposread|0x8                          |Force a position update                                  |
|useencoder|0x9                          |Enable VESC encoder                                      |
|offset|0xA                          |Get or set encoder offset                                |


## Other mainclasses:

### CAN debug bridge

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|main.0|0x1                          |CAN Bridge                                       |
|This class is GVRET/SavvyCAN compatible!

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|can   |0x0                          |Send a frame or get last received frame                  |
|rtr   |0x1                          |Send a RTR frame                                         |
|spd   |0x2                          |Change or get CAN baud                                   |


---

### TMC debug bridge

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|main.0|0x1                          |TMC Debug Bridge: Compatible with TMCL-IDE. |

To use the FOC modes position; velocity and torque you first must manually select the encoder and wait for alignment.

|Command name|CMD ID                       | Description                                             |
|------|-----------------------------|---------------------------------------------------------|
|id    |0x80000001                   |ID of class                                              |
|name  |0x80000002                   |name of class                                            |
|help  |0x80000003                   |Prints help for commands                                 |
|cmduid|0x80000005                   |Command handler index                                    |
|instance|0x80000004                   |Command handler instance number                          |
|selId |0x80000006                   |Selection id used to create this class                   |
|torque|0x0                          |Change torque and enter torque mode                      |
|pos   |0x1                          |Change pos and enter pos mode                            |
|openloopspeed|0x2                          |Move openloop. adr=strength;val=speed                    |
|velocity|0x3                          |Change velocity and enter velocity mode                  |
|mode  |0x4                          |Change motion mode                                       |
