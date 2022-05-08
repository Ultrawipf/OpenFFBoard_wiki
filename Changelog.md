Compiling changelogs from previous releases

## Firmware
#### v1.8.x
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


