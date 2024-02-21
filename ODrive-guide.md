# ODrive Configuration to Work with a Hoverboard Motor and MT6835 Encoder

## Genuine ODrive Setup

If using a genuine ODrive (only available directly from ODrive, not sold on AliExpress or the like), you can follow the instructions in the appropriate ODrive Getting Started guide in their documentation. For ODrive 3.6 and earlier, [use this one](https://docs.odriverobotics.com/v/0.5.6/index.html). For ODrive S1 and ODrive Pro, [use the latest version of the guide](https://docs.odriverobotics.com/v/latest/index.html). In either case, you should follow the instructions to update the firmware to the latest version before proceeding. Please follow the guide from the start and work your way through step by step. If you have trouble configuring your ODrive, the best option for support is the [ODrive Discord server](https://discord.gg/k3ZZ3mS). The ODrive team is active and helpful. Once you have the ODrive able to control your motor, contine to 


## Clone ODrive Setup

If you have an ODrive clone (found often on AliExpress from Makerbase or Flipsky), it is based on ODrive 3.5 and comes with a very old version of the firmware. You'll need to use [the old version of the guide](https://docs.odriverobotics.com/v/0.5.6/index.html). ODrive does not offer support for these devices, so your best bet is probably to ask in the [OpenFFBoard discord server](https://discord.com/servers/openffboard-704355326291607614).

### ODrive DFU Driver Setup 

**Before getting started, make sure correct drivers are installed for DFU interface. If you have ever installed Thrustmaster force feedback drivers, you will need to uninstall them to be able to update firmware on your ODrive or OpenFFBoard USB interface**

1. **Download Zadig**: [Zadig - USB driver installation made easy](https://zadig.akeo.ie/)
2. Set ODrive to DFU mode. This will vary depending on the board you have. Some have 2 DIP switches, one marked `DFU` and `RUN`, some have jumpers. If you have DIP switches, flip the switch to `DFU`. If you have jumpers, generally you'll need to remove the DFU jumper. If neither of these work, you'll need to find out from the manufacturer how DFU mode works on your device.
3. Connect ODrive to PC.
4. Open Zadig

![](img/odrive/zadig_window.png)

5. In the `Options` menu, select `List All Devices`

![](img/zadig_listall.png)

6. Find the Device called `STM32 BOOTLOADER`

![](img/odrive/zadig_drop_down.png)

If the `Driver` box on the left reads `WinUSB` with a version number, you can move to updating the firmware, otherwise proceed to step 7

7. Use the buttons to scroll through the driver options and select WinUSB and click the `Replace Driver` button. This will install the correct driver and can take a while. 

 ![](img/odrive/zadig_buttons.png)

 Once you see the success dialog box, click close and the Zadig window should look like the image below with the driver matching in both boxes. Close Zadig and continue to installing ODrive firmware

 ![](img/odrive/zadig_success.png)


## ODrive Firmware

### <ins>**If you have a non-genuine/fake ODrive with an old firmware or shows v0.0.0 please do this part!!**</ins>

1. Download and install STM32CubeProgrammer: [STM32CubeProg - STM32CubeProgrammer software for all STM32 - STMicroelectronics](https://www.st.com/en/development-tools/stm32cubeprog.html)
2. Download the firmware for your drive (I'm currently using v0.5.4 for a v3.6 56v Odrive): [Releases · odriverobotics/ODrive](https://github.com/odriverobotics/ODrive/releases)
3. Put the Odrive into DFU mode and plug it in. (Remove the DFU jumper if you have jumpers otherwise put the dipswitch to the DFU side and power it up)<br><br>
   <img src="img/ODrive Setup Images/OD_DFU_Jumper.jpg"  width="897"/><br>
   <img src="img/ODrive Setup Images/OD_DFU_Switch.jpg"  width="897"/>




5. Follow these steps:
   


   https://github.com/GameRiot6408/OpenFFBoard_wiki/assets/159271841/697b1e07-a518-4032-bc48-b0411dcc1464



### <ins>**If you have a genuine/original ODrive with an old firmware:**</ins>

1. Download the firmware for your drive (I'm currently using v0.5.4 for a v3.6 56v Odrive): [Releases · odriverobotics/ODrive](https://github.com/odriverobotics/ODrive/releases)
2. Put the Odrive into DFU mode and plug it in. (Remove the DFU jumper if you have jumpers otherwise put the dipswitch to the DFU side and power it up)<br><br>
   <img src="img/ODrive Setup Images/OD_DFU_Jumper.jpg"  width="897"/><br>
   <img src="img/ODrive Setup Images/OD_DFU_Switch.jpg"  width="897"/>

3. Type `odrivetool dfu <location of the firmware file>` like this.
<img src="img/ODrive Setup Images/OD_Firmware_Command.png"/>

4. Press 'Y' when it asks you to, and you should be good to go.

## ODrive Configuration to Work with the FFBoard

### **All Modifications have been done to the default configuration!**


### If you can’t save, it’s because the ODrive isn’t in Idle state so run this command if you have an issue:

`odrv0.axis0.requested_state = AXIS_STATE_IDLE`

1. Initialize the odrive tool by typing odrivetool (one word) in the CMD.
2. Paste in the below commands one by one (hit enter after each one).

    <span style="color:red;">These commands should start with the name of the ODrive (probably either dev0 or odrv0)</span>
    <img src="img/ODrive Setup Images/OD_Name.png"/>



    `odrv0.axis0.motor.config.pole_pairs = 15`<br>
   <span style="color:green;"># Common value for hoverboard motors</span>
    
    `odrv0.axis0.motor.config.torque_constant = 1`<br>
   <span style="color:green;"># If you know the KV value of the motor do this and change the value “8.27/(motor KV)” otherwise keep it at 1 </span>
    
    `odrv0.axis0.motor.config.current_lim = 10`<br>
   <span style="color:green;"># Set this value to bit below the max Amp value of your PSU mine was 12.5A so I used 10</span>
    
    `odrv0.config.enable_brake_resistor = True`<br>
   <span style="color:green;"># Sets use Brake resistor function</span>
    
    `odrv0.config.brake_resistance = 2`<br>
   <span style="color:green;"># Set the value to the Ohm value of your brake resistor. Mine came with a 2Ohm resistor</span>
    
    `odrv0.axis0.encoder.config.cpr = 65536`<br>
   <span style="color:green;"># Default value for the MT6835 encoder. Multiply this value accordingly if you have and gearing other than 1:1</span>
    
    `odrv0.axis0.config.startup_motor_calibration = True`<br>
   <span style="color:green;"># Makes ODrive run motor calibration on each startup</span>
    
    `odrv0.axis0.config.startup_encoder_offset_calibration = True`<br>
   <span style="color:green;"># Make ODrive perform an encoder offset calibration on each startup</span>
    
    `odrv0.axis0.config.startup_closed_loop_control = True`<br>
   <span style="color:green;"># Puts ODrive to the mode that is needed for the FFBoard to be able to control the ODrive automatically on startup</span>
    
    `odrv0.axis0.controller.config.enable_vel_limit = False`<br>
   <span style="color:green;"># Makes ODrive ignore Velocity limits. This command is very important otherwise the motor won’t function properly. Mine didn’t return to the center automatically with the spring force.</span>
    
    `odrv0.axis0.controller.config.enable_overspeed_error = False`<br>
   <span style="color:green;"># Makes it ignore set speed limits</span>
    
    `odrv0.can.config.baud_rate = 1000000`<br>
   <span style="color:green;"># Sets ODrive CAN baudrate</span>
    
    `odrv0.axis0.config.can.node_id = 0`<br>
   <span style="color:green;"># Sets ODrive CAN bus to work on ID 0</span>
    
    `odrv0.axis0.controller.config.control_mode = CONTROL_MODE_TORQUE_CONTROL`<br>
   <span style="color:green;"># Sets control mode to torque control</span>
    
    `odrv0.axis0.controller.input_torque = 1`<br>
   
    `odrv0.save_configuration()`<br>
   <span style="color:green;"># Save config</span>

   ### It should reboot itself now and go to Closed Loop Control mode.
 
 
 ## FFBoard Setup

1. Download and Open the Open FFBoard Configurator.exe: [OpenFFBoard releases](https://github.com/Ultrawipf/OpenFFBoard/releases)
2. Select the FFBoard and connect to it.
3. Go to the Axis:0 tab and change motor driver to Odrive and click change driver.<br> <img src="img/ODrive Setup Images/FFB_Motor_Controller.png"/>

4. Then go to the ODrive tab that appeared and click on Change CAN Settings and set it baudrate to 1000K. Apply it and press Ok.<br> <img src="img/ODrive Setup Images/FFB_CAN_Settings.png"/>
<br> <img src="img/ODrive Setup Images/FFB_CAN_Baudrate.png"/>

5. Set max torque range to your motor specs and Axis CAN ID to 0 and hit Submit. Then you will see some values in the info segment of this tab after a few seconds.<br><img src="img/ODrive Setup Images/FFB_Motor_Settings.png"/>

6. Hit Save to Flash at the bottom right corner on any tab.<br><img src="img/ODrive Setup Images/FFB_Save.png"/>

   

   ### You Should be good to go now!



