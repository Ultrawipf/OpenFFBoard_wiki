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


## FAQ

**When will it be available?**

No idea. Hopefully this year (not in large quantities yet.... So probably mid next year). Prototypes are ordered and have to be tested. First boards go to developers that want to help with the firmware.

**How much will it cost?**

From my estimates of parts and manufacturing a full kit should be available under 150€ if no unforeseen costs come up. No promises on that though. Might be less or slightly more to cover the costs.

**How much current does the TMC driver provide?**

Its designed for 20A (Most motors are fine with under 10A and plenty strong). With a 1mOhm shunt you can get it up to 30A+

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
