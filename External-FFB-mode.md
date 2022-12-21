## External FFB mode

The external FFB mainclass (id 3, `sys.main=3` to enable) is a normal HID gamepad without PID effects. Instead the effects can be managed using serial or HID commands with the usual command system. Check out [FFB manager commands](https://github.com/Ultrawipf/OpenFFBoard/wiki/Commands#effects-manager) for a list of commands.

Effects can be conditional or non conditional or periodic and have a type id.

### Normal effects
* Constant force = 1
  
A constant force effect has only a magnitude value (and scaler per axis) and applies this magnitude directly as a constant output torque.

### Periodic effects
* Ramp = 2
* Square = 3
* Sine = 4
* Triangle = 5
* Sawtooth up/down = 6/7

Periodic effects have a magnitude and period and can also have an envelope and phase which is not currently accessible in this mode.

### Conditional effects
* Spring = 8
* Damper = 9
* Inertia = 10
* Friction = 11
  
Conditional effects have condition blocks per axis with a saturation and coefficient value. The coefficient is different from the maginitude because there can be a different one for each axis.

A high coefficient makes a strong spring or damper for example.

#### Note:
Each effect has to be created first and enabled. The FFB state also must be enabled to change from idle mode to FFB effect mode.

Check out the [python examples](https://github.com/Ultrawipf/OpenFFBoard/tree/master/doc/python) on how to control effects via the HID protocol.