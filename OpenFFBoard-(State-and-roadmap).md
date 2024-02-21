## What is working well:
### FFBWheel mode

#### Force feedback wheels with the TMC4671:
The setup procedure is not optimal but a FFB wheel with servos or steppers with ABN and SinCos encoders run great in most games.

#### PWM output:
For other motor drivers you can use different PWM modes and output the calculated torque effect value as PWM. You need an ABN encoder connected to the FFBoard.

#### Button inputs:
You can select multiple button sources which will be combined into a gamepad button field of 32 buttons (maybe more later if needed. 32 is a common limit for HID, some programs support up to 128.)
SPI, Thrustmaster wheels, the onboard digital inputs and a shifter are possible button sources.

#### Shifter:
Analog joystick style shifters like the G29, G27 and G25 for example can connect to analog inputs and a reverse button (SPI for G27 or digital pin for G29) and you will get 6+1 gears as buttons.

#### Analog inputs:
6 analog pins are available as gamepad axes (pedals...) with optional autoranging and can be disabled individually.

#### Emergency stop:
An E-Stop pin can be pulled down on the STM board to stop the FFB.
For added security, the enable pin on the TMC can also be pulled down externally.
The emergency state can be reset when releasing or toggling the pin again if the STM board was used.

#### ODrive support:
An ODrive can receive torque commands and report the encoder position via a CAN bus for FFB.
Manual configuration of the ODrive required!

#### VESC support:
A VESC can receive torque commands and report the encoder position via a CAN bus for FFB.
Manual configuration of the VESC required!

#### Simplemotion support:
Experimental but working. May occasionally drop packets in case the IONI does not respond.
All setup must be done in the Granite tool.

#### Multi axis FFB for joysticks and flight sims:
Working with ODrive (And modified TMC boards). No special features implemented yet. Works mostly like the steering wheel mode but with 2 axes.

## General

#### Writing and dumping setups into and from flash
Back up of settings or quick start presets

#### HID control
Setting steering angles or strength from external programs without the serial port.
Great for third party applications and automations.
Works with almost all integrated commands.

#### MT6825 Encoder
Can be used with SPI3 with PWM and TMC motor drivers

#### BiSS-C Encoder
Can be used with SPI3 with PWM and TMC motor drivers

#### Autoalignment of steering wheels at startup:
With absolute encoders or encoders with home pulse, an absolute position can be searched at powerup and automatically set the center offset. Not possible with all encoders and motor drivers. Works with absolut encoders and ABN with index with TMC

## Planned features

#### Better TMC initialization routines for encoder alignment:
Important for safe and stable startup

***


#### SimHub integration via HID:
Auto change steering degrees and intensity depending on game. Motor stats as overlay etc.

#### Predefined settings and limiting options for specialized setups:
The FFBoard firmware is flexible so for different hardware, features have to be disabled or predefined

#### More 2 axis features
Automatic centering with mechanical endstops

