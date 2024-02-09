# ODrive Configuration to Work with a Hoverboard Motor and MT6835 Encoder


## ODrive Driver Setup

**Before getting started, change the ODrive drivers to libusb-win32:**

1. **Download Zadig**: [Zadig - USB driver installation made easy](https://zadig.akeo.ie/)
2. Connect ODrive to PC.
3. Follow this (you might need to do the same in DFU mode too maybe. It will show up as STM Bootloader):


## ODrivetool Setup

1. **Install Python**: [Download Python](https://www.python.org/)
2. Open up command prompt (CMD) and type `pip install odrive`.
3. Initialize the odrive tool by typing `odrivetool` (one word) in the CMD.

## ODrive Firmware

**If you have a non-genuine/fake ODrive with an old firmware or shows v0.0.0 please do this part!!**

1. Download and install STM32CubeProgrammer: [STM32CubeProg - STM32CubeProgrammer software for all STM32 - STMicroelectronics](https://www.st.com/en/development-tools/stm32cubeprog.html)
2. Download the firmware for your drive (I'm currently using v0.5.4 for a v3.6 56v Odrive): [Releases · odriverobotics/ODrive](https://github.com/odriverobotics/ODrive/releases)
3. Put the Odrive into DFU mode.
![ODrive with DFU jumper removed](https://drive.google.com/uc?export=view&id=1msPYKlTC1R43lDNciWIuL_1Wxdf8BIfr)

5. Follow these steps:


**If you have a genuine/original ODrive with an old firmware:**





1. Download the firmware for your drive (I'm currently using v0.5.4 for a v3.6 56v Odrive): [Releases · odriverobotics/ODrive](https://github.com/odriverobotics/ODrive/releases)
2. Put the Odrive into DFU mode. (remove the DFU jumper if you have jumpers otherwise put the dipswitch to the DFU side and power it up) 
![ODrive with DFU jumper removed](https://drive.google.com/uc?export=view&id=1msPYKlTC1R43lDNciWIuL_1Wxdf8BIfr)

4. Type `odrivetool dfu <location of the firmware file>` like this.
![Firmware upgrade command in CMD](https://drive.google.com/uc?export=view&id=1LU9gIeqIuxuMa5HkpPPRF_KPGTUB-RTs)

5. Press 'Y' when it asks you to, and you should be good to go.

## ODrive Configuration to Work with the FFBoard

**All Modifications have been done to the default configuration!**


## If you can’t save, it’s because the ODrive isn’t in Idle state so run this command if you have an issue:

`odrv0.axis0.requested_state = AXIS_STATE_IDLE`

1. Initialize the odrive tool by typing odrivetool (one word) in the CMD.
2. Paste in the below commands one by one (hit enter after each one).

    <span style="color:red;">These commands should start with the name of the ODrive (probably either dev0 or odrv0)</span>
    ![ODrive name](https://drive.google.com/uc?export=view&id=1HX4Ykw-8kYCfg2bMHWP10pyirMOALUgM)



    `odrv0.axis0.motor.config.pole_pairs = 15`
   + # Common value for hoverboard motors@@
    
    `odrv0.axis0.motor.config.torque_constant = 1`
   <span style="color:green;"># If you know the KV value of the motor do this and change the value “8.27/(motor KV)” otherwise keep it at 1</span>
    
    `odrv0.axis0.motor.config.current_lim = 10`
   <span style="color:green;"># Set this value to bit below the max Amp value of your PSU mine was 12.5A so I used 10</span>
    
    `odrv0.config.enable_brake_resistor = True`
   <span style="color:green;"># Sets use Brake resistor function</span>
    
    `odrv0.config.brake_resistance = 2`
   <span style="color:green;"># Set the value to the Ohm value of your brake resistor. Mine came with a 2Ohm resistor</span>
    
    `odrv0.axis0.encoder.config.cpr = 65536`
   <span style="color:green;"># Default value for the MT6835 encoder. Multiply this value accordingly if you have and gearing other than 1:1</span>
    
    `odrv0.axis0.config.startup_motor_calibration = True`
   <span style="color:green;"># Makes ODrive run motor calibration on each startup</span>
    
    `odrv0.axis0.config.startup_encoder_offset_calibration = True`
   <span style="color:green;"># Make ODrive perform an encoder offset calibration on each startup</span>
    
    `odrv0.axis0.config.startup_closed_loop_control = True`
   <span style="color:green;"># Puts ODrive to the mode that is needed for the FFBoard to be able to control the ODrive automatically on startup</span>
    
    `odrv0.axis0.controller.config.enable_vel_limit = False`
   <span style="color:green;"># Makes ODrive ignore Velocity limits. This command is very important otherwise the motor won’t function properly. Mine didn’t return to the center automatically with the spring force.</span>
    
    `odrv0.axis0.controller.config.enable_overspeed_error = False`
   <span style="color:green;"># Makes it ignore set speed limits</span>
    
    `odrv0.can.config.baud_rate = 1000000`
   <span style="color:green;"># Sets ODrive CAN baudrate</span>
    
    `odrv0.axis0.config.can.node_id = 0`
   <span style="color:green;"># Sets ODrive CAN bus to work on ID 0</span>
    
    `odrv0.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL`
   <span style="color:green;"># Sets control mode to torque control</span>
    
    `odrv0.axis0.controller.input_torque = 1`
   
    `odrv0.save_configuration()`
   <span style="color:green;"># Save config</span>

 ### <span style="color:green;">It should reboot itself now and go to Closed Loop Control mode.</span>

 ## FFBoard Setup

1. Download and Open the Open FFBoard Configurator.exe: [Release OpenFFBoard v1.14.2 · Ultrawipf/OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard/releases/tag/v1.14.2) 
2. Select the FFBoard and connect to it.
3. Go to the Axis:0 tab and change motor driver to Odrive and click change driver.
4. Then go to the ODrive tab that appeared and click on Change CAN Settings and set it baudrate to 100K. Apply it and press Ok.
5. Set max torque range to your motor specs and Axis CAN ID to 0 and hit Submit. Then you will see some values in the info segment of this tab after a few seconds.
6. Hit Save to Flash at the bottom right corner.

    ### You Should be good to go now!



