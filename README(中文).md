
##### 硬件准备,将hex文件写入lgt8f328p-ssop20
以下命令在ubuntu下使用,其它环境请作适当修改

+ 带arduino的lgt8f328p-ssop20板子,连接好串口到PC,使用如下命令写入:
```bash
avrdude -C/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyUSB0 -b115200 -D -Uflash:w:LarduinoISP_F328PS20.hex:i 
```
`-b115200`是指定bootloader能串口速率,请根据你的larduino的bootloader支持的串口速率适当修改.

+ lgt8f328p-ssop20空片需要连接小白盒,使用如下命令写入:
```bash
avrdude -C/etc/avrdude.conf -v -patmega328p -cjtag2isp -Pusb -Uflash:w:LarduinoISP_F328PS20.hex:i 
```

##### 使用说明
将写入完成的lgt8f328p-ssop20板子通过串口连接到PC,断开dtr与复位引脚的连接,避免进入内置的arduino bootloader.
通过如下连接到要烧写的lgt8f328p系列芯片
`PB5` -> `SWC`  
`PB4` -> `SWD`  
`PB1` -> `RST`  


+ 使用命令行写入芯片时,使用命令
```bash
avrdude -C/etc/avrdude.conf -v -patmega328p -cstk500v1 -P/dev/ttyUSB0 -Uflash:w:your_app_lgt8f328p.hex:i
```

+ Arduino IDE中选择编程器为`AVR ISP`,端口选择所连的串口,即可使用IDE中的`烧录引导程序`和`使用编程器上传`两项菜单功能.


仅适用于烧录LGT8F328P系列芯片

[来自:https://blog.csdn.net/nicechao/article/details/102875388](https://blog.csdn.net/nicechao/article/details/102875388)

