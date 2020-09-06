![Logo](img/ffboard_logo.svg)
# Open FFBoard

The _Open FFBoard_ is an open source firmware (and hardware) project for DIY force feedback devices like for example simracing steering wheels ranging from budget DC motor builds up to high end servo direct drive wheels.

Together with a [custom motor driver and usb interface](https://github.com/Ultrawipf/OpenFFBoard-hardware) this project is made for developers and enthusiasts to create their dream setup within a reasonable budget.

The firmware is designed to be easily extendable and to be reconfigured at runtime by the users.

This means the firmware can control different kinds of motors and motor drivers (Stepper, 3 Phase BLDC, DC) motors, read encoder positions and present itself as a force feedback gamepad to the computer via HID.

Having the HID PID part implemented in a modular way allows it to be used in different ways without the need to write complex custom USB descriptors.
