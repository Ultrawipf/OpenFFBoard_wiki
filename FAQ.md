## FAQ

**Which motor drivers are supported?**

* PWM output with locally connected encoder
* Custom TMC4671 based driver with ABZ, SinCos and 3 Phase analog encoders
* ODrive via CAN
* VESC via CAN
* more to come...

**I can not connect in DFU mode**

* You need a winusb DFU driver. Use [Zadig](http://zadig.akeo.ie/) to install it.
* If you already have a driver loaded with the name "Guillemot STM DFU Device" unfortunately thats Thrustmaster overwriting your driver. This driver is not compatible with any normal DFU tool and must be uninstalled first.

**When will it be available?**

Prototypes are made and have to be tested. The parts availability unfortunately prevents making any large batch at the moment.

**How much will it cost?**

Considering the rapidly changing prices of components its hard to say. 
Check out the [tindie store page](https://www.tindie.com/stores/gigawipf/) for updated prices.

**How much current does the TMC driver provide?**

Its designed for around 20-25A (Most motors are fine with under 10A and plenty strong). A different current sensor can allow for a larger or smaller range.

** Can i use a stepper driver (TS6600, HB860, or similar...) **

No. These drivers are not actual FOC drivers even if they use an encoder to correct missed steps.
They are not capable of driving the motor with a constant force. You will need the TMC4671 driver for steppers or a different supported driver.

**I want it super cheap and don't need servos. Is that possible without the TMC?**

Yes. For really simple setups a halfbridge DC motor driver and encoder can be connected directly to the FFBoard (STM Interface) instead of using the TMC driver.
This way you can also use some third party motor drivers with PWM inputs.

**What's Difference between BLDC and PMSM servo?**

It's (basically) the same motor type.
PMSM (permanent magnet stator motor) = BLDC (Brushless Direct Current Motor) = ac synchronous (three phase synchronous motors).
Three phases with a permanent magnet is all the same no matter if you call it BLDC, Servo, AC-Motor. As long as its got a magnet (as rotor) and has three phases its the same motor type.

**How can I donate?**

[Patreon](https://www.patreon.com/gigawipf) or [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=B23BD5FGD5CH8&source=url)

**How can I help?**

There needs to be done a lot of testing and debugging. Therfore if you have **c++** experience and/or have a motor to test with join our [discord](https://discord.gg/gHtnEcP).
