# Compatibility list

Non exhaustive list of tested games.
All fully directinput compatible games should work but some games may use whitelists for specific devices or require config modifications.

|Symbol  |Status|
|-----------|-------|
|:white_check_mark:|**Fully working**<br>(Only ingame setup required at most)|
|:ballot_box_with_check: | **Fully working** with non invasive modifications<br>or external config changes for correct operation |
|:warning:  | **Partially or with issues**<br>(May need third party tools, significant effort or has issues impacting gameplay) |
|:x:  |**Not working** at all or significant problems<br>(Not officially supported)|
|:memo:|Notes available below|



|Game  |Status|
|-----------|-------|
| Assetto corsa |:white_check_mark:|
| Assetto corsa competizione|:white_check_mark:|
| Automobilista 2 |:white_check_mark:|
| EA WRC |:ballot_box_with_check: :memo: (See below)|
| Forza horizon 4 |:ballot_box_with_check: :memo:  (See below)|
| Forza horizon 5 |:ballot_box_with_check: :memo:  (See below)|
| Dirt Rally 2.0 |:ballot_box_with_check: :memo: (config mod)|
| Dirt Rally |:ballot_box_with_check: :memo: (config mod)|
| Dirt 4 |:ballot_box_with_check: :memo: (config mod)|
| F1 2020 |:white_check_mark: :memo: (See note)|
| F1 2022 |:white_check_mark: :memo: (See note)|
| rFactor 2 |:white_check_mark:|
| BeamNG |:white_check_mark:|
| KartKraft |:white_check_mark:|
| Project Cars 1 |:white_check_mark:|
| Project Cars 2 |:white_check_mark:|
| WRC 8 |:white_check_mark: :memo: |
| WRC Generations |:white_check_mark: :memo: |
| Trackmania 2020 |:white_check_mark:|
| DCS World |:white_check_mark: (2 axis joystick)|
| IRacing |:white_check_mark:|
| Euro Truck Simulator 2 |:white_check_mark:|
| Raceroom |:white_check_mark:|
| Live for Speed |:white_check_mark:|
| Wreckfest |:white_check_mark:|
| F1 CHALLENGE 99-02 |:white_check_mark:|
| Mud Runner |:white_check_mark:|
| Snow Runner |:x: (Whitelisted vendors<br/>Registry hack possible)|
| Moto GP 22 |:x: (xinput only)|
| Richard Burns Rally |:warning: :memo: (Registry mod)|
| CarX | :warning: (Bad FFB in general reported)|
| Garfield Kart | :warning: (No FFB :smirk:)|
| Sébastien Loeb Rally EVO |:x: :warning: (Crashes in control mapper<br/>Maybe fixable or unrelated?)|
| Dakar Desert Rally|:warning: (FFBoard works but other devices may interfere)|

# Setup procedures for specific games and recommended settings

## All Dirt games
Dirt requires you to add custom devices to the `device_defines.xml` for example found in the `DiRT Rally 2.0\input\devices` path or similar.


Add this line to `device_defines.xml`:

`<device id="{FFB01209-0000-0000-0000-504944564944}" name="openffboard" priority="100" type="wheel" official="false" />`


You can also add a `openffboard.xml` to the actionmaps folder:
```
<?xml version="1.0" encoding="utf-8"?>
<action_map name="openffboard" device_name="openffboard" library="lib_direct_input">
  <axis_defaults>
    <axis name="di_x_axis">
    <action deadzone="0" name="driving.steer.left" />
    <action deadzone="0" name="driving.steer.right" />
    </axis>
  </axis_defaults>
  <group name="driving">
    <group name="steer">
      <action name="left">
       <axis name="di_x_axis" type="lower" />
      </action>
     <action name="right">
      <axis name="di_x_axis" type="upper" />
    </action>
  </group>
 </group>
</action_map>
```

Recommended settings:
|Setting  |Value|
|-----------|-------|
|CF Filter  |50-80hz|
|CF Filter q|0.3-0.7|
|Range      |540    |

## EA WRC
Wheel may not be detected or not have any force feedback.  In the file `steamapps\common\EA SPORTS WRC\WRC\Content\input\Windows\devices\device_defines.xml` add this line : 

    <device id="{FFB01209-0000-0000-0000-504944564944}" name="openffboard" priority="100" type="wheel" official="false" />

Add a new file `openffboard.xml` in `steamapps\common\EA SPORTS WRC\WRC\Content\input\Windows\actionmaps` with the following content:

    <?xml version="1.0" encoding="utf-8"?>
    <action_map name="openffboard" device_name="openffboard" library="lib_direct_input" version="2">
      <axis_map>
        <axis name="di_x_axis" direction_type="left_right" axis_set_name="device"/>
      </axis_map>
      <axis_defaults>
        <axis name="di_x_axis">
          <action deadzone="0" name="driving.steer.left" />
          <action deadzone="0" name="driving.steer.right" />
        </axis>
      </axis_defaults>
      <group name="driving">
        <group name="steer">
          <action name="left">
            <axis name="di_x_axis" type="lower" />
          </action>
          <action name="right">
            <axis name="di_x_axis" type="upper" />
          </action>
        </group>
      </group>
    </action_map>

## F1 Games

Disable all steering assists.

There will still be a gamepad style visual steering wheel wobble or assist in the simulated wheel for non whitelisted devices. Not confirmed if it impacts the actual input or is only visual.

Recommended settings:
|Setting  |Value|
|-----------|-------|
|Range      |360    |

## WRC Games

The games use the spring effect for FFB. Confirmed for WRC 8 and WRC Generations.
Consider playing around with the spring gain to set how direct and stiff it feels.

More FFB tuning options available in `steamapps\common\WRCxxx\Common\Settings\InputFFBSoftwareConfig.cfg`


Recommended settings:
|Setting  |Value|
|-----------|-------|
|Range      |540    |
|Spring gain |10 - max|

## Richard Burns Rally
Richard Burns Rally requires a key to be added to Windows registry. This can be done by creating a `RBR_openffboard.reg` file with this content:
```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\System\CurrentControlSet\Control\MediaProperties\PrivateProperties\Joystick\OEM\VID_1209&PID_FFB0]
"OEMData"=hex:43,00,88,01,fe,00,00,00
```
Warning: This may change the behaviour in other games.


## Forza Horizon 5 (or others)
The OpenFFBoard works with Forza in theory but might be more stable with emuwheel.

Invert FFB force direction in game or use emu wheel.

Recommended settings:
|Setting  |Value|
|-----------|-------|
|CF Filter  |60-200hz|
|CF Filter q|0.3-0.7|
|Range      |540    |

<details>
<summary>Config file</summary>

Adding a file `DefaultRawGameControllerMappingProfileOpenFFBoard.xml` to the media/inputmappingprofiles.zip might force it to be the primary steering device. 

**It is not confirmed if this actually helps at all so you may not need that.**

```
<Profiles>
<RawGameControllerInputMappingProfile Version="1" Id="a5dcbf10-6530-11d2-901f-00c04fb951ed" UserFacingName="IDS_DefaultWheelProfile_OpenFFBoard_Name" IsDefaultProfile="1" PrimaryDeviceVidPid="0x1209FFB0" FFBDeviceVidPid="0x1209FFB0" FFBMotorIndex="0">

  <!-- Race -->
  <Context Version="1" Context="INPUTCONTEXT_RACING">
    <Value Version="1" Key="INPUTCMD_GAS" VidPid="0x044fb67f" InputType="Axis" Index="1" InvertAxis="false" InnerDeadzone="0." OuterDeadzone="1.00" />
    <Value Version="1" Key="INPUTCMD_BRAKE" VidPid="0x044fb67f" InputType="Axis" Index="2" InvertAxis="false" InnerDeadzone="0." OuterDeadzone="1.00" />
    <Value Version="1" Key="INPUTCMD_CLUTCH" VidPid="0x044fb67f" InputType="Axis" Index="3" InvertAxis="false" InnerDeadzone="0." OuterDeadzone="1.00" />
    <Value Version="1" Key="INPUTCMD_STEERING" VidPid="0x044fb67f" InputType="Axis" Index="0" InvertAxis="false" DeadzonesAroundCenter="false" InnerDeadzone="0.00" OuterDeadzone="1.00" />  
  </Context> 
  <Context Version="1" Context="INPUTCONTEXT_RACING_UI">
  </Context>
```
</details>

## Games working with vjoy emuwheel
### Forza

Also confirmed working if you still have other issues is [emuwheel](https://forzatools.weebly.com/forza-emuwheel-setup-guide.html). 

Emuwheel will merge and hide multiple devices into one virtual one getting around some of the issues forza has with incompatible devices.
It will also forward FFB effects to the steering wheel device.

This tool works for games that have steering wheel whitelists blocking unknown devices but supporting vjoy.

In Dakar Desert Rally only 1 vjoy device can be present or it may use the wrong one. Sometimes it works. Sometimes not. For now unsupported.
