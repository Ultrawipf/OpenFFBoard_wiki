Compiling changelogs from previous releases

## Firmware

#### v1.14.x
- TMC E-Stop handled even during calibration by pausing and disabling driver
- E-Stop checked correctly after startup. You can now disable force and delay startup by setting E-Stop during startup.
- Digital and Analog sources are disabled by default
- Biss-C 1 rotation offset glitch at first packet fixed
- Reverted CAN retransmission to enabled temporarily. Fixes 2 axis ODrive issues.
- Save TMC space vector PWM mode in flash. Should be usually on for BLDC motors if the star point is isolated.
- Allow using the motors flux component to dissipate energy with the TMC4671 instead of the brake resistor. May cause noticable braking in the motor but takes stress off the resistor.
- Axis speed limiter usable and saved in flash.
- Removed unused hall direction flash setting.
- Added local button pulse mode
- Only activate brake resistor if vint and vext are >6.5V. Prevents board from activating resistor if only usb powered and a fault reset loop
- Changed behaviour of direction enable and axis enable bits in set_effect report to always apply direction vector
    Fix for Forza Motorsport


#### v1.13.x
- Added basic iterative TMC PI autotuning
- Fixed issues with CAN transmission with multiple axes
- Added SSI encoder support (AMT232B)
- Fixed SPI buttons not working (SPI2 DMA on F407)
- Dynamic TMC encoder alignment current based on current limit

#### v1.12.x
- Added part of unique serial number to usb interface names for easier identification of multiple devices
- Added support for Simplemotion V2 (Ioni/Argon motor drivers)
- Fixed a possible crash if unparsable/too large numbers are sent in a command
- Removed unused direction field from descriptor in 2 axis desc
- Workarounds for 2 axis conditional effects giving condition blocks priority over direction angles
- Added new subproject for third party devkits (F407DISCO target)
- Added serialfx effect manager for a command based FFB mainclass (Instead of PID FFB)
- Added Serial FFB mainclass mode
- Added mosfet BBM time to TMC hardware selection
- TMC enable pin is set when TMC debug mode starts
- Added option to change SPI speed for buttons. Can be helpful if the connection is unreliable
- Added back second VESC instance for 2 axis vesc setups
- Separate motor driver selection lists per axis (No double odrive/vesc/tmc instance options in motor driver lists)


#### v1.11.x
- Added new subproject for third party devkits (F407DISCO target)
- Added serialfx effect manager for a command based FFB mainclass (Instead of PID FFB)
- Added Serial FFB mainclass mode
- Added mosfet BBM time to TMC hardware selection
- TMC enable pin is set when TMC debug mode starts
- Added option to change SPI speed for buttons. Can be helpful if the connection is unreliable
- Added back second VESC instance for 2 axis vesc setups
- Separate motor driver selection lists per axis (No double odrive/vesc/tmc instance options in motor driver lists)

#### v1.10.x
- Added local encoder index option to reload a previously stored offset
- Fixed an issue with 2 axis FFB effects on second axis
- Added TMC4671 biquad filter option
  - Lowpass, notch and peak modes (fixed Q factor, saved frequency)
- Improved BISS performance when used with TMC
- Fixed an issue with live effects statistics jumping to 0 using double buffers
- Added missing command flags and help messages
- Changed default power from 2000 to 5000 as 2000 is not enough to calibrate many motors
- Internal change moving effects into effectscalculator to simplify managing effects from different sources
- Effect intensity tuning value now only affects game effects. Fixes the effect intensity incorrectly affecting the endstop.

#### v1.9.6
- Added analog filter option
- Main effect loop runs in higher priority thread than idle
- Added ADS111X analog source
- Added user configurable axis encoder ratios for setups with reductions
- Added effect filter option (Speed/accel filter presets for different encoders)
- Added effects monitoring
- Added some analog autorange margin
- Added min/max commands to analog processing for manual ranges
- Added analog processing functions to ADS111X
- Selecting a "none" encoder will remove the axis value. Allows analog inputs to be used as the primary axis.
- Added constant force rate command
- Highly improved uart command stability (default baud rate 115200)
- Added command to check command flags (cls.cmdinfo?cmdid)
- Added advanced filter mode to switch between custom and default conditional effect output filters ("fx.filterProfile_id")
- Automatic flash erase condition changed from major version change to separate flash version counter

#### v1.8.8
- Rescaled endstop to encoder angle (makes strength feel the same at every range)
- Changed SPI button saved count from 0-63 to 1-64 (will invalidate your setting)
- Added CAN next frame length command to send frames with different headers
- Emergency stop can be reset and only disables torque
- Added estop command
- Optimized string based command interfaces
- Effects honor the gain setting (Makes Forza Horizon work)

#### v1.8.7
- FFBWheel and FFBJoystick classes split for 1 and 2 axis FFB (Allows to use different HID descriptors)
- Added a single axis HID descriptor (currently not used for compatibility reasons. enable by defining FFBWHEEL_USE_1AXIS_DESC)
- Default SPI button speed increased to 1.3MHz
- Added CAN button source
- Added CAN analog source
- Moved CAN and i2c speed settings to port class
- Fixed CAN bridge RTR frames
- HID interface sends ACKs
- Improved help command formatting and added flags
- Added I2C fast mode 400kHz
- Added BISS-C encoder
- Fixed MT Encoder
- Reworked TMC external encoder system
- Digital and analog source readout command

#### v1.7.4

*  F407 reboots correctly after exiting DFU bootloader
*  Added I2C helper classes and support for PCF8574 button sources
*  More efficient task activation using notifications instead of semaphores where possible
*  Fixed hex parsing in commands (xFF equivalent to 255 shortening commands for very long values)
*  Option to forward SPI encoders to TMC for commutation or combining TMC and axis position sources
*  Improved linux compatibility
*  Fixed effect envelope handling
*  Updated to tinyusb 0.13
*  Reports 64 buttons in descriptor


#### v1.6.x

- Additional buffer checks for command interfaces
- Improves stability of HID command interface while broadcasting changes
- Reset to factory defaults/erasing flash if major version differs or flash seems locked (experimental. might fix writing issues)
- Smaller bug fixes regarding odrive & vesc & encoders
- VESC CAN id selection added


## Configurator

#### v1.14.x
- Disabled tmc autotune button for DC and None motors
- Added Axis position readout
        TODO: axis.cpr will be changed to be consistent with axis.pos in firmware and not report TMC encoder cpr anymore -> encoder tuning resolution will display incorrect again and needs fixing
- Added task list window
- Fixed some issues in DFU flashing
- Added TMC space vector PWM checkbox
- Added option to prefer energy dissipation in motor for TMC instead of brake resistor
- Added speed limiter axis option
- Added basic translation function
- Fixed CS selection in SPI buttons
- Added axis output torque to FX live graph


#### v1.13.x
- Fixed issue in encoder tuning UI
- Added SSI encoder ui


#### v1.9.6
- Added analog filter option
- Added ADS111X source dialog
- Added manual range tuning option for local analog and ADS111X
- Automatically connects at startup if one supported FFBoard device is found
- Many small fixes for stability
- Added update browser (Help->updates)
- Added automatic update notifications for firmware and GUI if detected
- Redesigned UI layout
- Added effect monitoring windows
- Added advanced effect tuning window
- Added encoder filter tuning window
- Added basic profile management system
- Added encoder gear reduction option (For belt/gear driven wheels if there is a reduction between the wheel and encoder. Prescales all internal positions)
- Added constant force rate readout


#### v1.8.7
- Fixed crash when applying vesc settings

#### v1.8.6
- Split 1 and 2 axis mainclasses
- Added CAN button source
- Added analog CAN source
- fast mode for PCF buttons
- Moved CAN settings to common dialog
- BISS-C encoder support
- TMC graph follows system style
- Windows darkmode support
- Digital and analog readout

#### v1.7.2

- Support for TMC autohoming
- Support for I2C PCF8574 button source
- TMC full calibration button added
- Added TMC encoder notices
- Shows flux in TMC graph and total current
- Changed icon



## Changelog Hardware

Status: *IN DEVELOPMENT! Not a final design*


Info:
If you experience issues with the stability/usb connection/noise with the TMC driver and the FFBoard in versions until including 1.2.2 try to isolate the middle 2 standoffs between the stm and tmc board or replace them with nylon standoffs. 
It seems like they are a bit too closely coupled to the power part of the driver and cause a ground loop depending on your setup.
In the next version i will try to increase the impedance and path length a bit between the power and the digital sections.
Increasing the groundplane distance reduces noise coupled in from the power stage.

### TMC Driver:

#### 1.1: (Prerelease prototype)
- Added filtering for Hall and Encoder inputs.
- Separated TMC and STM VM sense dividers

#### 1.2: (Major redesign)
- Using TMC4671-LA production version
- Added 5V buck converter
- Added emergency shutdown method by pulling enable low
- Rotated power stage. Moved all motor connectors to one side
- Moved analog encoder pins and routed differential inputs out
- Improved vcore impedance
- Increased encoder filter frequencies
- Reduced resistance of sense dividers
- Switched LM5050 to LM74700
- Space for 2 VM capacitors
- Improved mosfet protection
- Added temperature sensor pads on AGPI-B
- 50x50+100mm screw holes

#### 1.2 fix:
- Fixed silkscreen (R18 and R19 swapped)
- Modified some labels
- Added 33k gate pulldown for brake resistor
- Moved and resized vias in motor driver part (Manufacturing reliability)
- Tented vias

#### 1.2.2 (HALL):
- Redesigned power stage to use hall sensors (LEM GO SME and TMCS1100)
- Changed buffers to 74LV17APWJ
- Added opamp for TMC inputs (temperature and voltage sensing)
- Used opamp as comparator for hardware brake resistor activation point (~65V)

#### 1.3:
- Using stronger MAX5035 DC converter
- Significantly lower sensor noise
- Using separate 5V LDO for analog sensors
- Using ACS742 30A current sensors
- Different MOSFETS
- Parallel gate diodes
- Better reliability


### STM USB Interface:
#### 1.1:
- Initial prototype
- STM32F411RE based
- Only supports TMC4671 driver
- Only one SPI2 CS

#### 1.2:
- STM32F407VG
- Reserved PWM pins
- 3 CS pins per SPI
- CAN bus
- Reserved E-Stop
- USB Vbus sense
- separated ADCs for vsense and analog in
- LEDs moved
- Added FFBoard logo
- Changed USB diode to SMC
- Added zener pad on 5V
- Removed encoder buffer
- Higher value pwr led resistor

#### 1.2.1:
- Fixed some labels
- Moved USB socket and terminals slightly to the corners (Big usb plugs might interfere with the pins)
- Changed crystal load capacitors to lower values. (F407 DFU is very sensitive and does not work reliably with too high value caps)
- Added E-Stop capacitor against noise triggering it
- Tented vias

#### 1.2.2
- Swapped (Previously unused) Encoder Z pin from pin 65 to pin 62 because of interrupt conflicts with the DRV flag pin

#### 1.2.3
- USB-C instead of micro USB
- SPI1 uses a 2 row header
- Additional USB protections
