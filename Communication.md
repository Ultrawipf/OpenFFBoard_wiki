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


Some HID relevant values can also be used via HID IN and OUT reports.
The report contains a type, address and value.
See `hid_cmd_defs.h` for available ids.