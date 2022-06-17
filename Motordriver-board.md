## Changelog Hardware

Status: *IN DEVELOPMENT! Not a final design*


Info:
If you experience issues with the stability/usb connection/noise with the TMC driver and the FFBoard in versions until including 1.2.2 try to isolate the middle 2 standoffs between the stm and tmc board or replace them with nylon standoffs. 
It seems like they are a bit too closely coupled to the power part of the driver and cause a ground loop depending on your setup.
In the next version i will try to increase the impedance and path length a bit between the power and the digital sections.
Increasing the groundplane distance reduces noise coupled in from the power stage.

### TMC Driver:

#### 1.1: (Prerelease prototype)
- Added filtering for Hall and Encoder inputs.
- Separated TMC and STM VM sense dividers

#### 1.2: (Major redesign)
- Using TMC4671-LA production version
- Added 5V buck converter
- Added emergency shutdown method by pulling enable low
- Rotated power stage. Moved all motor connectors to one side
- Moved analog encoder pins and routed differential inputs out
- Improved vcore impedance
- Increased encoder filter frequencies
- Reduced resistance of sense dividers
- Switched LM5050 to LM74700
- Space for 2 VM capacitors
- Improved mosfet protection
- Added temperature sensor pads on AGPI-B
- 50x50+100mm screw holes

#### 1.2 fix:
- Fixed silkscreen (R18 and R19 swapped)
- Modified some labels
- Added 33k gate pulldown for brake resistor
- Moved and resized vias in motor driver part (Manufacturing reliability)
- Tented vias

#### 1.2.2 (HALL):
- Redesigned power stage to use hall sensors (LEM GO SME and TMCS1100)
- Changed buffers to 74LV17APWJ
- Added opamp for TMC inputs (temperature and voltage sensing)
- Used opamp as comparator for hardware brake resistor activation point (~65V)

### STM USB Interface:
#### 1.1:
- Initial prototype
- STM32F411RE based
- Only supports TMC4671 driver
- Only one SPI2 CS

#### 1.2:
- STM32F407VG
- Reserved PWM pins
- 3 CS pins per SPI
- CAN bus
- Reserved E-Stop
- USB Vbus sense
- separated ADCs for vsense and analog in
- LEDs moved
- Added FFBoard logo
- Changed USB diode to SMC
- Added zener pad on 5V
- Removed encoder buffer
- Higher value pwr led resistor

#### 1.2.1:
- Fixed some labels
- Moved USB socket and terminals slightly to the corners (Big usb plugs might interfere with the pins)
- Changed crystal load capacitors to lower values. (F407 DFU is very sensitive and does not work reliably with too high value caps)
- Added E-Stop capacitor against noise triggering it
- Tented vias

#### 1.2.2
- Swapped (Previously unused) Encoder Z pin from pin 65 to pin 62 because of interrupt conflicts with the DRV flag pin

#### 1.2.3
- USB-C instead of micro USB
- SPI1 uses a 2 row header
- Additional USB protections
