Compiling changelogs from previous releases

## Firmware

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
### v1.9.6
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

* Support for TMC autohoming
* Support for I2C PCF8574 button source
* TMC full calibration button added
* Added TMC encoder notices
* Shows flux in TMC graph and total current
* Changed icon
