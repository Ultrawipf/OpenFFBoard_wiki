## Commands:

### Syntax for string based Interfaces. (CDC and UART):

#### Baudrate
* Default baudrate for UART: 500000
* For CDC (USB) baudrate setting has no effect. It will send as fast as possible.

#### Request format:
Get: `cls.(instance.)cmd?` or `cls.(instance.)cmd?adr`

Set: `cls.(instance.)cmd=val` or `cls.(instance.)cmd=val?adr`

Info `cls.(instance.)cmd!` sometimes used for generating a list of supported options. Check source code for mode info.

Values can be supplied as hex (`x4d2`) or base 10 (`1234`). 

Commands with 2 values are rarely used. One example is setting a register in the TMC or passing a CAN frame with a target address and value.

#### Reply format:
`[cls.instance.cmd?|val]` or `[cls.instance.cmd?|val:adr]` for get commands

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

Replies to request commands will reply as a request as well as any other broadcast of changed values.

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
            val = struct.unpack('<q', bytes(data[9:17]))
            addr = struct.unpack('<q', bytes(data[17:25]))
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

Commands marked as "Debug" are treated as invalid if the sys.debug variable is not set to 1 first.
They can be (even more) dangerous and possibly damage hardware if misused. That does not mean all others are safe! 
Commands marked as "STR" or "I" type requests are not available for HID as they return a string.
Be careful when changing motor parameters. Incorrect settings can damage the hardware or cause injury.

|Flag     |Description|Example   |
|---------|-----------|----------|
|R        |Read or Execute|cls.cmd?  |
|W        |Write value|cls.cmd=10|
|RA       |Read with address|cls.cmd?20|
|WA       |Write with address|cls.cmd=10?20|
|I        |Get special info string (Not available for HID)|cls.cmd!  |

### System commands
|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|sys.0 |0x0                          |System Commands                                          |


|Command name|CMD ID|Description                                          |Flags |
|------------|------|-----------------------------------------------------|------|
|help        |0x0   |Print system help                                    | (STR)|
|save        |0x1   |Write all settings to flash                          | R    |
|reboot      |0x2   |Reset chip                                           | R    |
|dfu         |0x3   |reboot into DFU bootloader                           | R    |
|lsmain      |0x6   |List available mainclasses                           | R    |
|lsactive    |0x8   |List active classes (Fullname:clsname:inst:clsid:idx)| R    |
|vint        |0xE   |Internal voltage(mV)                                 | R    |
|vext        |0xF   |External voltage(mV)                                 | R    |
|main        |0x7   |Query or change mainclass                            | R W  |
|swver       |0x4   |Firmware version                                     | R    |
|hwtype      |0x5   |Hardware type                                        | R    |
|flashraw    |0xD   |Write value to flash address                         | WA   |
|flashdump   |0xC   |Read all flash variables (val:adr)                   | R    |
|errors      |0xA   |Read error states                                    | R    |
|errorsclr   |0xB   |Reset errors                                         | R    |
|heapfree    |0x11  |Memory info                                          | R    |
|format      |0x9   |set format=1 to erase all stored values              | W    |
|debug       |0x13  |Enable or disable debug commands                     | R W  |
|devid       |0x14  |Get chip dev id and rev id                           | R    |



Note for HID:
The lsactive command will report the class id in the value field and the instance number in the address field. 
That way it is possible to check which modules are available.

---

### FFB Wheel&Joystick

Commands apply to both 1 axis and 2 axis FFB HID mainclasses

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|main.0      |0x1       |FFB Wheel (1 Axis): Force feedback HID game controller|
|main.0      |0x2       |FFB Joystick (2 Axis): Force feedback HID game controller|

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|ffbactive   |0x0       |FFB status                                            | R        |
|btntypes    |0x2       |Enabled button sources                                | R W      |
|addbtn      |0x4       |Enable button source                                  | W        |
|lsbtn       |0x3       |Get available button sources                          | R (STR)  |
|aintypes    |0x5       |Enabled analog sources                                | R W      |
|lsain       |0x6       |Get available analog sources                          | R (STR)  |
|addain      |0x7       |Enable analog source                                  | W        |
|hidrate     |0x8       |Get estimated effect update speed                     | R        |
|hidsendspd  |0x9       |Change HID gamepad update rate                        | R W I    |
|estop       |0xA       |Emergency stop                                        | R W      |




---

### FFB effects
|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|fx.0  |0xA02                        |Effects: Controls internal FFB effects                   |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|filterCfFreq|0x0       |Constant force filter frequency                       | R W      |
|filterCfQ   |0x1       |Constant force filter Q-factor                        | R W      |
|spring      |0x3       |Spring gain                                           | R W I    |
|friction    |0x4       |Friction gain                                         | R W I    |
|damper      |0x5       |Damper gain                                           | R W I    |
|inertia     |0x6       |Inertia gain                                          | R W I    |
|effects     |0x2       |List effects. set 0 to reset                          | R W (STR)|


---

### FFB axis

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|axis.0|0xA01                        |Axis: FFB axis                                           |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|power       |0x0       |Overall force strength                                | R W      |
|degrees     |0x1       |Rotation range in deg                                 | R W      |
|esgain      |0x2       |Endstop stiffness                                     | R W      |
|zeroenc     |0x3       |Zero axis                                             | R        |
|invert      |0x4       |Invert axis                                           | R W      |
|idlespring  |0x5       |Idle spring strength                                  | R W      |
|axisdamper  |0x6       |Independent damper effect                             | R W      |
|enctype     |0x7       |Encoder type get/set/list                             | R W I    |
|drvtype     |0x8       |Motor driver type get/set/list                        | R W I    |
|pos         |0x9       |Encoder position                                      | R        |
|maxspeed    |0xA       |Speed limit in deg/s                                  | R W      |
|maxtorquerate|0xB       |Torque rate limit in counts/ms                        | R W      |
|fxratio     |0xC       |Effect ratio. Reduces effects excluding endstop. 255=100%| R W      |
|curtorque   |0xD       |Axis torque                                           | R        |
|curpos      |0xE       |Axis position                                         | R        |



---

### MT SPI encoder

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|mtenc.0|0x62                         |MT6825 SPI3                                              |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|cs          |0x0       |CS pin                                                | R W      |
|pos         |0x1       |Position                                              | R W      |
|errors      |0x2       |Parity error count                                    | R        |

---

### SPI buttons

|Prefix      |Class ID  |Class description                                     |
|------------|----------|------------------------------------------------------|
|spibtn.0    |0x22      |SPI Buttons 1: SPI 2 Button                           |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|mode        |0x0       |SPI mode                                              | R W I    |
|btncut      |0x1       |Cut buttons right                                     | R W      |
|btnpol      |0x2       |Invert                                                | R W      |
|btnnum      |0x3       |Number of buttons                                     | R W      |
|cs          |0x4       |SPI CS pin                                            | R W      |


---

### Digital pin buttons

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|dpin.0|0x21                         |D-Pins: Digital pin button source                        |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|mask        |0x0       |Enabled pins                                          | R W      |
|polarity    |0x1       |Pin polarity                                          | R W      |
|pins        |0x2       |Available pins                                        | R W      |
|values      |0x3       |pin values                                            | R        |


---

### Analog shifter buttons

Supports G25,G27 (w. all SPI buttons),G29 and similar type shifters w. 2 axis analog stick and reverse button

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|shifter.0   |0x23      |Shifter Analog: Analog 6+1 gear shifter button source|

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|mode        |0x0       |Shifter mode                                          | R W I    |
|x12         |0x1       |X-threshold for 1 2 gears                             | R W      |
|x56         |0x2       |X-threshold for 5 6 gears                             | R W      |
|y135        |0x3       |Y-threshold for 1 3 5 gears                           | R W      |
|y246        |0x4       |Y-threshold for 2 4 6 gears                           | R W      |
|revbtn      |0x5       |Pin for R signal                                      | R W      |
|cspin       |0x6       |CS pin for SPI modes                                  | R W      |
|xchan       |0x7       |X signal analog pin                                   | R W      |
|ychan       |0x8       |Y signal analog pin                                   | R W      |
|vals        |0x9       |Analog values                                         | R        |
|gear        |0xA       |Decoded gear                                          | R        |



---

### PCF8574 buttons

|Prefix       |Class ID  |Class description                                        |
|-------------|----------|---------------------------------------------------------|
|pcfbtn.0     |0x24      |I2C PCF8574: btnnum/8 devices required. Addresses starting at 0x20.|

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|btnnum      |0x0       |Amount of buttons                                     | R W      |
|invert      |0x1       |Invert buttons                                        | R W      |
|speed       |0x2       |400kb/s mode                                          | R W      |

---

### CAN buttons

|Prefix      |Class ID  |Class description                                     |
|------------|----------|------------------------------------------------------|
|canbtn.0    |0x25      |CAN Buttons                                           |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|btnnum      |0x0       |Amount of buttons                                     | R W      |
|invert      |0x1       |Invert buttons                                        | R W      |
|canid       |0x2       |CAN frame ID                                          | R W      |


---

### Analog pin axes

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|apin.0|0x41                         |AIN-Pins: Analog pins source                             |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|mask        |0x0       |Enabled pins                                          | R W      |
|autocal     |0x1       |Autoranging                                           | R W      |
|pins        |0x2       |Available pins                                        | R W      |
|values      |0x3       |Analog values                                         | R        |


--- 

### CAN analog axes

|Prefix      |Class ID  |Class description                                     |
|------------|----------|------------------------------------------------------|
|cananalog.0 |0x42      |CAN Analog: 4 16b axes per 64b packet                 |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|canid       |0x0       |CAN frame ID of first packet. Next packet ID+1        | R W      |
|amount      |0x1       |Amount of analog axes                                 | R W      |
|maxamount   |0x2       |Maxmimum amount of analog axes                        | R        |


---


### PWM motor driver

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|pwmdrv.0|0x84                         |PWM: PWM output motor driver                             |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|freq        |0x1       |PWM period selection                                  | R W I    |
|mode        |0x0       |PWM mode                                              | R W I    |


---

### TMC4671 motor driver

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|tmc.0 |0x81                         |TMC4671: TMC4671 interface                               |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|cpr         |0x0       |CPR in TMC                                            | R W      |
|mtype       |0x1       |Motor type                                            | R W I    |
|encsrc      |0x2       |Encoder source                                        | R W I    |
|tmcHwType   |0x3       |Version of TMC board                                  | R W I    |
|encalign    |0x4       |Align encoder                                         | R        |
|poles       |0x5       |Motor pole pairs                                      | R W      |
|acttrq      |0x6       |Measure torque and flux                               | R        |
|pwmlim      |0x7       |PWM limit                                             | R W (DEBUG)|
|torqueP     |0x8       |Torque P                                              | R W      |
|torqueI     |0x9       |Torque I                                              | R W      |
|fluxP       |0xA       |Flux P                                                | R W      |
|fluxI       |0xB       |Flux I                                                | R W      |
|velocityP   |0xC       |Velocity P                                            | R W      |
|velocityI   |0xD       |Velocity I                                            | R W      |
|posP        |0xE       |Pos P                                                 | R W      |
|posI        |0xF       |Pos I                                                 | R W      |
|tmctype     |0x10      |Version of TMC chip                                   | R        |
|pidPrec     |0x11      |PID precision bit0=I bit1=P. 0=Q8.8 1= Q4.12          | R W      |
|phiesrc     |0x12      |PhiE source                                           | R W (DEBUG)|
|fluxoffset  |0x13      |Offset flux scale for field weakening                 | R W      |
|seqpi       |0x14      |Sequential PI                                         | R W      |
|iScale      |0x15      |Counts per A                                          | (STR)    |
|encdir      |0x16      |Encoder dir                                           | R W (DEBUG)|
|abnpol      |0x1F      |Encoder polarity                                      | R W      |
|temp        |0x17      |Temperature in C * 100                                | R        |
|reg         |0x18      |Read or write a TMC register at adr                   | WA RA (DEBUG)|
|svpwm       |0x19      |Space-vector PWM                                      | R W      |
|autohome    |0x1D      |Find abn index                                        | R        |
|abnindex    |0x1C      |Enable ABN index                                      | R W      |
|calibrate   |0x1A      |Full calibration                                      | R        |
|calibrated  |0x1B      |Calibration valid                                     | R        |
|state       |0x1E      |Get state                                             | R        |
|combineEncoder|0x20      |Use TMC for movement. External encoder for position   | R W      |
|invertForce |0x21      |Invert incoming forces                                | R W      |
|vm          |0x22      |VM in mV                                              | R        |
|extphie     |0x23      |external phie                                         | R        |


---

### ODrive motor driver (CAN)
Example here is only M0. M1 is available too.

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|odrv.0|0x85                         |ODrive (M0): ODrive motor driver with CAN                |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|canid       |0x0       |CAN id of ODrive                                      | R W      |
|canspd      |0x1       |CAN baudrate                                          | R W      |
|errors      |0x2       |ODrive error flags                                    | R        |
|state       |0x3       |ODrive state                                          | R        |
|maxtorque   |0x4       |Max torque to send for scaling                        | R W      |
|vbus        |0x5       |ODrive Vbus                                           | R        |
|anticogging |0x6       |Set 1 to start anticogging calibration                | W        |
|connected   |0x7       |ODrive connection state                               | R        |



---

### VESC motor driver

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|vesc.0|0x87                         |VESC: VESC CAN interface                                 |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|offbcanid   |0x0       |CAN id of OpenFFBoard Axis                            | R W      |
|vesccanid   |0x1       |CAN id of VESC                                        | R W      |
|canspd      |0x2       |CAN baud (3=250k 4=500k 5=1M)                         | R W      |
|errorflags  |0x3       |VESC error state                                      | R        |
|vescstate   |0x4       |VESC state                                            | R        |
|voltage     |0x5       |VESC supply voltage (mV)                              | R        |
|encrate     |0x6       |Encoder update rate                                   | R        |
|pos         |0x7       |VESC position                                         | R        |
|torque      |0x8       |Current VESC torque                                   | R        |
|forceposread|0x9       |Force a position update                               | R        |
|useencoder  |0xA       |Enable VESC encoder                                   | R W      |
|offset      |0xB       |Get or set encoder offset                             | R W      |

--- 

## Ports
### CAN port

|Prefix      |Class ID  |Class description                                     |
|------------|----------|------------------------------------------------------|
|can.0       |0xC01     |Can port                                              |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|speed       |0x0       |CAN speed preset (0:50k;1:100k;2:125k;3:250k;4:500k;5:1M)| R W I    |
|send        |0x1       |Send CAN frame. Adr&Value required                    | WA       |

---

### I²C port

|Prefix      |Class ID  |Class description                                     |
|------------|----------|------------------------------------------------------|
|i2c.0       |0xC02     |I2C port                                              |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|speed       |0x0       |I2C speed preset (0:100k;1:400k)                      | R W I    |

---

## Other mainclasses:

### CAN bridge

|Prefix|Class ID                     |Class description                                        |
|------|-----------------------------|---------------------------------------------------------|
|main.0|0x1                          |CAN Bridge (This class is GVRET/SavvyCAN compatible!)    |

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|can         |0x0       |Send a frame or get last received frame               | R WA     |
|rtr         |0x1       |Send a RTR frame                                      | WA R     |
|spd         |0x2       |Change or get CAN baud                                |R W       |


---

### TMC debug bridge

Debug mode must be active for this to show up

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
|~~selId~~ |~~0x80000006~~                   |~~Selection id used to create this class~~                   |
|torque|0x0                          |Change torque and enter torque mode                      |
|pos   |0x1                          |Change pos and enter pos mode                            |
|openloopspeed|0x2                          |Move openloop. adr=strength;val=speed                    |
|velocity|0x3                          |Change velocity and enter velocity mode                  |
|mode  |0x4                          |Change motion mode                                       |

--- 

### MIDI

Debug mode must be active for this to show up

|Prefix      |Class ID  |Class description                                     |
|------------|----------|------------------------------------------------------|
|main.0      |0x1       |MIDI (TMC): Easteregg mainclass to play midi songs on the tmc|

|Command name|CMD ID    |Description                                           |Flags     |
|------------|----------|------------------------------------------------------|----------|
|id          |0x80000001|ID of class                                           | R        |
|name        |0x80000002|name of class                                         | R (STR)  |
|help        |0x80000003|Prints help for commands                              | R I (STR)|
|cmduid      |0x80000005|Command handler index                                 | R        |
|instance    |0x80000004|Command handler instance number                       | R        |
|power       |0x0       |Intensity                                             | R W      |
|range       |0x1       |Range of phase change                                 | R W      |
