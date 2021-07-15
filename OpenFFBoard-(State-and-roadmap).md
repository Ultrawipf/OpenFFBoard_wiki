<div align="center">
    <a href="https://github.com/Ultrawipf/OpenFFBoard">
        <img width="100" height="100" src="img/ffboard_logo.svg">
    </a>
	<br>
	<br>
	<div style="display: flex;">
		<a href="https://discord.gg/gHtnEcP">
            <img src="https://img.shields.io/discord/704355326291607614">
		</a>
		<a href="https://github.com/Ultrawipf/OpenFFBoard/stargazers">
            <img src="https://img.shields.io/github/stars/Ultrawipf/OpenFFBoard">
		</a>
	</div>
</div>
<br>


## What is working well:
FFBWheel mode:

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

#### ODrive support:
An ODrive can receive torque commands and report the encoder position via a CAN bus for FFB.
Manual configuration of the ODrive required!


## Planned features:

#### HID control of certain parameters:
Setting steering angles or strength from external programs without the serial port.
Currently in development.

#### Better TMC initialization routines for encoder alignment:
Important for safe and stable startup

#### Multi axis FFB for joysticks and flight sims:
Complex. Will take time but planned in the future

#### Odrive support:
Interesting for multi axis ffb.

#### CAN bus:
Using the FFBoard as a CAN bus interface or adding analog/digital inputs via CAN.

#### External encoder support for TMC:
Tunneling BISS-C or EnDat through the STM to the TMC as a position source. Would be very flexible but adds communication overhead

#### Writing and dumping setups into and from flash:
Back up of settings or quick start presets

#### SimHub integration via HID:
Auto change steering degrees and intensity depending on game. Motor stats as overlay etc.

#### Predefined settings and limiting options for specialized setups:
The FFBoard firmware is flexible so for different hardware, features have to be disabled or predefined

#### Improving GUI stability and setup procedures:
The setup is still a bit unstable depending on how its done. Maybe a wizard could help.

#### Improving TMC Debug bridge mainclass:
The TMC debug mainclass is very helpful for testing the driver with the Trinamic IDE (TMCL-IDE). The mainclass is hacky and not stable with the newest TMC ide.

#### Autoalignment of steering wheels at startup:
With absolute encoders or encoders with home pulse, an absolute position can be searched at powerup and automatically set the center offset. Not possible with all encoders and may require slow rotations.