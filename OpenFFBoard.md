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



## Changelog Hardware

Status: *IN DEVELOPMENT! Not a final design*

## Hardware features

The STM interface has additional pins available to use your hardware inputs.

You can connect pedals, handbrakes, shifters, potentiometers, buttons and more to be used as gamepad inputs.

A 32 bit timer for PWM generation is available for PPM and PWM motor drivers.

A brake resistor pin is available and can activate depending on the difference between V_INT and V_EXT analog inputs (3.3V. Scale with a divider.)

### Additional Inputs

Digital inputs: 8 Buttons - additional (up to 32) via SPI available with support for Thrustmaster wheels and PISO shift registers.<br>
Analog inputs: max. 6 analog inputs available.
