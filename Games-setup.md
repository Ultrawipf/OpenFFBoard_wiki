## Setup procedures for specific games


## All Dirt games:
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


## Richard Burns Rally:
Richard Burns Rally requires a key to be added to Windows registry. This can be done by creating a `RBR_openffboard.reg` file with this content:
```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\System\CurrentControlSet\Control\MediaProperties\PrivateProperties\Joystick\OEM\VID_1209&PID_FFB0]
"OEMData"=hex:43,00,88,01,fe,00,00,00
```


## Forza Horizon 5 (or others)

When only one FFBoard is connected it will also detect that but FFB forces may need to be inverted ingame. 
It will only work when the FFBoard is the first detected HID so you may need to temporarily disconnect other gamepads, pedals and other devices.

Also confirmed working: [emuwheel](https://forzatools.weebly.com/forza-emuwheel-setup-guide.html). 
Emuwheel will merge multiple devices into one virtual one getting around some of the issues forza has with multiple devices
