Note: This is currently not correct for the master branch. We will merge soon. In the master there is no echo of the sent command.

## Virtual serial port
Most of the configuration is done via a simple string based protocol.

Commands are ";" or "\n" separated.

You can send "help\n" to print all currently available help strings of active classes.

Usages:
Reading a value: <cmd>?;

Setting a value: <cmd>=<int>;

Setting a value as hex: <cmd>=xa5 (Note the x prefix)

Advanced commands:

Setting a value at address (dual values): <cmd>?<addr>=<val>

Getting a value at address (Getter with value): <cmd>?<addr>


The FFBoard will echo back the command and reply separated by a ":" and add a \n after each reply.

For most setters it will print back "OK" to acknowledge it.

Example of chained commands:
`lsain;power=10;power?;`

will print back:

`>power=10:OK\n`

`>power?:10\n`

`>lsain:0:AIN-Pins\n`

Note the ":" separator after the command. Can be easily split by splitting replies by \n and then by splitting the first ":" match into command and reply.

Sometimes a prefix can be used to address a specific instance of an axis for example like `X.power?;`

## HID
Some HID relevant values can also be used via HID IN and OUT reports.

The report contains a type, address and value.
```
        uint8_t	reportId = HID_ID_CUSTOMCMD; //HID_ID_CUSTOMCMD_FEATURE = 0xAF
	HidCmdType	type = HidCmdType::err;	// 0x01. Type of report. 0 = error, 1 = write, 2 = request
	uint32_t	cmd = 0;				// 0x02 Use this as an identifier for the command
	uint32_t	addr = 0;				// 0x03 Use this to transfer an optional address (CAN for example)
	uint64_t	data = 0;				// 0x04 Use this to transfer data
```
The ID of the report is 0xAF.
To write a value set the type to write (1) and set cmd as the command id (for example 0x20 for strength) and data as the actual data. Addr is an optional field which can contain additional data like an identifier. This is normally not used.
The device will respond by echoing the packet back so every listener on the system will be notified of the change.

For requesting a value use the type "read" = 2 and set the cmd id accordingly. The data field is ignored. The device will respond with a packet containing the actual data in the data field and the requested cmd id with the same packet.

Python example:
```
import pywinusb.hid as hid
import sys,time
import struct

# Receive and print data
def readData(data):
    if(data[0] == 0xAF):
        t = data[1]
        cmd = struct.unpack('<L', bytes(data[2:6]))
        addr = struct.unpack('<L', bytes(data[6:10]))
        data = struct.unpack('<Q', bytes(data[10:18]))
        print("Type {}, cmd {}, addr {}, data {}". format(t,cmd,addr,data))

def main():
    device = hid.HidDeviceFilter(vendor_id = 0x1209,product_id = 0xFFB0).get_devices()[0]
    device.open()
    print(device.find_output_reports())
    target_usage = hid.get_full_usage_id(0xff00, 0x01) # Vendor usage 1
    print(target_usage)
    device.set_raw_data_handler(readData)

    for report in device.find_output_reports():
        if target_usage in report:
            print("Found",report)
            report[hid.get_full_usage_id(0xff00, 0x01)]=1 # type. (1 = write, 2 = read)
            report[hid.get_full_usage_id(0xff00, 0x02)]=0x20 # cmd
            report[hid.get_full_usage_id(0xff00, 0x03)]=0 # addr (optional)
            report[hid.get_full_usage_id(0xff00, 0x04)]=100 # data
            report.send()

    while device.is_plugged():
        time.sleep(0.5)
    device.close()

if __name__ == '__main__':
    main()

```

See `hid_cmd_defs.h` for available ids.