## Changelog Hardware

Status: *IN DEVELOPMENT! Not a final design*

## TMC4671 motor driver:

### V1.2 Major Update

Using TMC4671-LA production version.<br>
Added 5V buck converter <br>
Added emergency shutdown method by pulling enable low<br>
Rotated power stage.<br>
Moved all motor connectors to one side.<br>
Moved analog encoder pins and routed differential inputs out.<br>
Improved Vcore impedance.<br>
Increased encoder filter frequencies.<br>
Reduced resistance of sense dividers.<br>
Switched LM5050 to LM74700.<br>
Space for 2 VM capacitors.<br>
Improved MOSFET protection.<br>
Added temperature sensor pads on AGPI-B<br>
Added 50x50+100mm screw holes<br>

### V1.1 Prerelease prototype

Added filtering for Hall and Encoder inputs.<br>
Separated TMC and STM VM sense dividers.

## Board informations

Hardware design of the TMC-driverboard can be found here: [Motordriver-Board](https://github.com/Ultrawipf/OpenFFBoard-hardware).<br>
The git includes the pcb design and the bill of materials to manufacture one for yourself.

## STM USB Interface:
### 1.2:
Switched from F411RE to F407VE for now (More pins and better availability)<br>
Added FFBoard logo<br>
Changed USB diode to SMC<br>
Added CAN transceiver<br>
SPI3 on ext header<br>
Added 3 CS pins for each of the SPI ports<br>
Added reserved emergency stop pin<br>