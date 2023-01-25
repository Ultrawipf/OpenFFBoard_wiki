## FAQ

**Which motor drivers are supported?**

* PWM output with locally connected encoder
* Custom TMC4671 based driver with ABZ, SinCos and 3 Phase analog encoders
* ODrive via CAN
* VESC via CAN
* Simplemotion v2
* more to come...

**I can not connect in DFU mode**

* You need a winusb DFU driver. Use [Zadig](http://zadig.akeo.ie/) to install it.
* If you already have a driver loaded with the name "Guillemot STM DFU Device" unfortunately thats Thrustmaster overwriting your driver. This driver is not compatible with any normal DFU tool and must be uninstalled first.

**When will it be available?**

Check out the [tindie store page](https://www.tindie.com/stores/gigawipf/).  The parts availability unfortunately prevents making any large batch at the moment so keep an eye on the discord and store.

**My chip stays in basic/failsafe mode and does not save settings**

This is a rare issue with the F407VG flash and it is unknown what causes it due to it being improssible to reproduce on demand.
The known fix is to do a full chip erase (using GUI  or STM32CubeProgrammer) and reflash the firmware. That usually fixes it for the rest of the lifetime of the chip. If it happens again it may need another erase cycle.

**How much current does the TMC driver provide?**

Its designed for around 20-25A (Most motors are fine with under 10A and plenty strong). A different current sensor can allow for a larger or smaller range.

** Can i use a stepper driver (TS6600, HB860, or similar...) **

No. These drivers are not actual FOC drivers even if they use an encoder to correct missed steps.
They are not capable of driving the motor with a constant force. You will need the TMC4671 driver for steppers or a different supported driver.

**I want it super cheap and don't need servos. Is that possible without the TMC?**

Yes. For really simple setups a halfbridge DC motor driver and encoder can be connected directly to the FFBoard (STM Interface) instead of using the TMC driver.
This way you can also use some third party motor drivers with PWM inputs.

**Does the TMC support induction motors?**

No. It supports PMSM/BLDC, DC and 2 phase stepper motors.

**How to use the brake resistor output with other motor drivers than the TMC**

Check the [pinouts](https://github.com/Ultrawipf/OpenFFBoard/wiki/Pinouts-and-peripherals#brake-resistor).
You can use a 297k/10k resistor divider on the Vint (after a diode at the driver) and Vext (before the diode at the power supply) to let the STM activate the brake resistor on the brake pin.

**How can I donate?**

[Patreon](https://www.patreon.com/gigawipf) or [PayPal](http://paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=B23BD5FGD5CH8)

**How can I help?**

There needs to be done a lot of testing and debugging. Therfore if you have **c++** experience and/or have a motor to test with join our [discord](https://discord.gg/gHtnEcP).
