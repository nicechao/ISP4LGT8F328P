##### LarduinoISP for LGT8F328P
running on LGT8F328P-SSOP20

+ Hardware connection  
`PB5` -> `SWC`  
`PB4` -> `SWD`  
`PB1` -> `RST`  


+ Command line example
```bash
avrdude -C/etc/avrdude.conf -v -patmega328p -cstk500v1 -P/dev/ttyUSB0 -Uflash:w:your_app_lgt8f328p.hex:i 
```

+ Arduino IDE choose `AVR ISP` programmer
