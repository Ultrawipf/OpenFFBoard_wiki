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


This is the OpenffBoard hardware wiki page. It provides an overview of already tested hardware.

## Disclaimer

At the moment the software is far from finished. Features may not work completely or contain errors. <br>
*THIS IS STILL IN DEVELOPMENT! NOTHING ON THIS PAGE IS GURANTEED TO WORK!*

## Table of Contents

| Table of Contents |
| --- |
|[Disclaimer](#Disclaimer)|
|[General](#General)|
|[Board](#Board)|
|[Motors](#Motors)|
|[Motordriver](#Motordriver)|
|[Encoders](#Encoders)|
|[Power supply](#Powersupply)|
|[Steeringwheels](#Steeringwheels)|
|[Cables](#Cables)|
|[Misc](#Misc)|

## General

The Open FFBoard is an open source force feedback interface with the goal of creating a platform for highly compatible simulation devices.
To enjoy it's full potential you need diffrent bits of hardware. Most notably a controller board aka. the OpenFFBoard, a motordriver, a motor and cables and a steeringwheel.
This page should provide you with an overview of tested hardware so you can decide what's useful for your rig.
Build instructions can be found here: [Setup](wiki/setup).


## Board

The OpenffBoard is based around a STM32 and serves mainly as USB HID interface to the computer. It's firmware is open source [OpenffBoard-Firmware](https://github.com/Ultrawipf/OpenFFBoard).
Detailed informations can be found on the dedicated OpenFFBoard Wiki page: [OpenFFBoard](wiki/OpenFFBoard).
Currently there is no option to buy the board (yet). But it's layout files and parts list can be found here [Hardware-Design](https://github.com/Ultrawipf/OpenFFBoard-hardware).
Therefore you are able to make one yourself or you can check the Discord for ongoing groupbuys [Discord](https://discord.gg/gHtnEcP).

<!---
##Prepped for nice pictures

<div align="center">
   <a href="https://github.com/Ultrawipf/OpenFFBoard-hardware">
       <img width="300" height="300" src="https://github.com/Ultrawipf/OpenFFBoard/doc/img/openFFboard_naked.jpg">
   </a>
</div>
--->
To drive one of the motors listed beneath you'll need a Motordriver-Board [Motordriver](#Motordriver)

## Motors

**This project is still in development. Recommended motors are not guaranteed to work but are well established in the simracing community.**

| Name | Capabilities | Estimated price | Where to buy |
| ---  |      ---     |       ---       |       ---    |
| 130ST-10010<br>Small Mige | Rated Power: 1000W<br>Rated Voltage: 220V<br>Rated Speed: 1000rpm<br>Rated Torque: 10Nm<br>Peak Torque: 20Nm<br>Torque coefficient: 2.2Nm/A | Please contact Mige directly for a quote.<br> The cost for shipping is significant.<br>Taxes and fees have to be paid. | Search for Mige on Alibaba.<br>It is not recommended to buy 3rd party. |
| 130ST-15015<br>Big Mige | Rated Power: 2300W<br>Rated Voltage: 220V<br>Rated Speed: 1500rpm<br>Rated Torque: 15Nm<br>Peak Torque: 30Nm<br>Torque coefficient: 1.58Nm/A | Please contact Mige directly for a quote.<br> The cost for shipping is significant.<br>Taxes and fees have to be paid. | Search for Mige on Alibaba.<br>It is not recommended to buy 3rd party. |
| 80ST-M04025 | Rated Power: 1000W<br>Rated Voltage: 220V<br>Rated Speed: 2500rpm<br>Rated Torque: 4Nm<br>Peak Torque: 12Nm<br>Torque coefficient: 0.9Nm/A | Please contact Mige directly for a quote.<br> The cost for shipping is significant.<br>Taxes and fees have to be paid. | Search for Mige on Alibaba.<br>It is not recommended to buy 3rd party. |
| SEM HR115C6 | Rated Power: 1.8kW<br>Rated Voltage: 530V<br>Rated Speed: 6000rpm<br>Rated Torque: 6.8Nm<br>Peak Torque: 20Nm<br>Torque coefficient: 1.1/A |  | Used from Ebay |
| 34HS59-5004D<br>Stepper | Amps/Phse: 5A<br>Voltage: 5V<br>Holding Torque: 13Nm<br>Step Angle: 1.8° | [stepperonline.com](https://www.omc-stepperonline.com/de/nema-34-schrittmotor-13-0nm-1841oz-in-w-bremse-reibmoment-4-0nm-566oz-in.html)  | ~120€ + Shipping (EU) |

**How to contact Mige?**

-Goto Mige on Alibaba: [Alibaba.com/mige](https://hzmgdj.en.alibaba.com/?spm=a2700.wholesale.cordpanyb.2.618c7790hddpKe)<br>
-Login or create an account<br>
-Click on "Contact supplier"<br>
-Type in which servomotor you want, ask for its price including shipping for the motor, cables and the better 10k encoder (if you want the 10k encoder).<br><br>
Lisa is very helpful and will answer in no time.

## Motordriver

The plug and play motordriver board is based around a TMC4671. It's design and firmware is also open-source and can be found here: [Hardware-Design](https://github.com/Ultrawipf/OpenFFBoard-hardware).<br>
It's current capabilities and features can be found here: [Motordriver-Board](wiki/Motordriver-board).

<!---
##Prepped for nice pictures

<div align="center">
    <a href="https://github.com/Ultrawipf/OpenFFBoard-hardware">
        <img width="150" height="150" src="https://github.com/Ultrawipf/OpenFFBoard/doc/img/tmcdriver.jpg">
    </a>
</div>
-->

## Encoders

Encoders that can be used with the current development. Some encoders can only be used as SinCos encoders.

| Name | PPR/CPR | Estimated price | Where to buy |
| ---  |      ---     |       ---       |       ---    |
| CUI AMT103 | Depends on version.<br>Up to 2048ppr or 8192cpr | [Digikey.de](https://www.digikey.de/product-detail/de/cui-devices/AMT103-V/102-1308-ND/827016) | ~20€ + Shipping |
| AMT132 | Depends on version.<br>Up to 4096ppr or 16384cpr | [Digikey.de](https://www.digikey.de/product-detail/de/cui-devices/AMT132S-V/102-6644-ND/10269185) | ~30€ + Shipping |
| E6B2CWZ6C | up to 2500ppr | [Digikey.de](https://www.digikey.de/product-detail/de/omron-automation-and-safety/E6B2-CWZ6C-1-200P-R/Z9418-ND/2670658) | ~400€ |
| AMS5115 | SinCos | -- | -- |
| EQN1325 | 4096ppr or 8192cpr | -- | -- |

## Power supply

Different motors need different power supplies. Compare this table from the Simucube deveopment for reference: [Power supply table](https://www.dropbox.com/s/mgn66se44pe0ab3/DIY%20DD%20Wheel%20Servo%20information%20Rev8.pdf?dl=0).<br>
Early tests suggest that the TMC-driver board is very efficient. With a Mige 130ST-15015 a 350 watt psu was sufficient even at very high torque settings.


## Steeringwheels

This is intended as modular as possible. Therefore no steeringwheels are provided. There are 3D-printable designs you can use. For a more sturdy setup consider using a clamping set.
(e.g. [Clamping set](https://www.maedler.de/product/1643/1621/spannsaetze-com-b-rostfrei-bohrung-10-bis-50mm) -> in case of a Mige servo use 22mm ID.)<br> 
Adapters and quick connects can also be bougth enabeling a fully customisable setup to your liking.

## Cables

When Ordering from Mige there are 3m cables already included. The included cables are shielded and can be used with the OpenFFBoard.<br> 
Power cables and the encoder need to be connected to the OpenffBoard trough a connector. Depending on the board design you need to order the correct connector type.

## Misc

Additional parts needed to build a complete working openFFBoard force feedback system.

### Braking resistor

A braking resistor is necessary to discharge the energy generated by the motor when used in generator mode. Without a braking resistor the generated voltage spikes will damage the power supply and the openFFBoard/TMC-Driver.<br>
It is recommended to use at least a 50 watt resistor with a ohms rating of 10 ohms to 20 ohms.

*VERY IMPORTANT:*
If powered by a power supply always have the resistor connected  through the active diode circuit (VM pin). Otherwise you have *NO WAY* to burn energy and you will kill everything if the board does not detect overvoltage and stop the driver. And even then it might be too late.
The resistor is activated in software from the Stm (early. depending on difference between internal and external voltage) and as a backup by the tmc (Close to overvoltage point). This means if the board is not powered or under reset the resistor won't activate and needs the buffer caps.
In the v1.2 TMC-hardware revision two EEU-FS1K681B with 680µF are used as buffer capacitor. So no external caps are needed.