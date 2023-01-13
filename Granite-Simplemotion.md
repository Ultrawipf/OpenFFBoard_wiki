TODO. Images coming soon

Check the [wiki pages for ionicube](https://granitedevices.com/wiki/IONICUBE_1X_connectors_and_pinouts) for pinouts.

It must be set up in Granity in torque mode and with STO and hardware enable pins set accordingly.


### Connections
Connect the following pins of the official OpenFFBoard to a RS485 transceiver (MAX585 breakout board for example)
* GP7 (TX) to DI
* GP8 (RX) to RO
* DRV_GP (On Motor header) to RE and DE. This switches the transceiver between transmit (LOW) and receive (HIGH).
* GND to GND
* 3.3V (or 5V if signal level is too low) to VCC of transceiver

Picture following soon....