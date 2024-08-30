## Linux FFB setup

### udev rules

OpenFFBoard uses the builtin hid-generic driver.  Unfortunately this has some undesirable
defaults such as a default deadzone, and a fuzz setting of 255. Here is a udev rule to
set deadzone and fuzz to 0 for all available axes.  The contents of `RUN` below will be
run automatically when OpenFFBoard is connected.

1. Create the file `/etc/udev/rules.d/98-openffboard.rules`.
2. Add the following in that file:
    ```
    SUBSYSTEM=="input", ATTRS{idVendor}=="1209", ATTRS{idProduct}=="ffb0", RUN+="/usr/bin/evdev-joystick --s '%E{DEVNAME}' --f 0 --d 0"
    ```
3. Reload the udev rules.
    ```
    sudo udevadm control --reload-rules
    ```
4. Trigger udev to run on currently connected devices.  Alternatively unplug the
OpenFFBoard and plug it back in.
    ```
    sudo udevadm trigger
    ```
5. Check to make sure the udev rule was applied, openffboard should report 0 for `flatness` and `fuzz`. (Requires the joyutils package)
    ```
    $ evdev-joystick --s /dev/input/by-id/usb-Open_FFBoard_FFBoard_*-event-joystick

      Absolute axis 0x00 (0) (X Axis) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
      Absolute axis 0x01 (1) (Y Axis) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
      Absolute axis 0x02 (2) (Z Axis) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
      Absolute axis 0x03 (3) (X Rate Axis) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
      Absolute axis 0x04 (4) (Y Rate Axis) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
      Absolute axis 0x05 (5) (Z Rate Axis) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
      Absolute axis 0x06 (6) (Throttle) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
      Absolute axis 0x07 (7) (Rudder) (value: 0, min: -32767, max: 32767, flatness: 0 (=0.00%), fuzz: 0)
    ```

### Known issues

* "Desktop Spring" does not work in linux as the hid-generic driver appears to send FFB data all of the time so the
 "No FFB" condition is never met.  The status indicator at the bottom right of the configurator will show `FFB 0hz (CF 0hz)`
 even when not in a game rather than changing color to indicate an idle state.  This has no impact on in-game performance.

#### Glossary:
* "fuzz" - Per the python-evdev documentation, this is a value used to filter noise from
 the event input stream resulting in a reduced resolution or "choppy" feel when changing
 direction, or sometimes continuously.
* "deadzone" - A range, usually at the center or beginning of an axis, where input in ignored
* "configurator" - The application used to adjust firmware settings for the openFFBoard, available [here](https://github.com/Ultrawipf/OpenFFBoard-configurator)
