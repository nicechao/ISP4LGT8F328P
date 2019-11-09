#!/usr/bin/python3

import sys
import re

filename="Wave.txt"
def load_packet():
    ds=[]
    with open(filename) as fp:
        #pattern = re.compile('^([\d.]+)(m|n|u)s\s+0\s+([01])\s+([01])$')
        pattern = re.compile('^([\d.]+)(m|n|u)s\s+([01])\s+([01])$')
        last_swc=1
        time_swc=0
        idx_swc = 4
        idx_swd = 3
        for line in fp.readlines():
            line = line.strip()
            m = pattern.match(line)
            if m:
                t = float(m.group(1))
                if m.group(2)=="m":
                    t = t*1000
                elif m.group(2)=="n":
                    t = t/1000

                swc = int(m.group(idx_swc))
                if swc!=last_swc:
                    if not swc:
                        start_swc = t
                        high = t - time_swc
                        time_swc = t
                    else:
                        low = t-start_swc
                        time_swc = t
                        #swd = int(m.group(idx_swd))
                        #记录上一次取样的swd
                        d = (swd, high, low)
                        ds.append(d)
                    last_swc = swc
                swd = int(m.group(idx_swd))
    return ds
ds = load_packet()

dn = len(ds)
n=0
while n<dn:
    d = ds[n]
    n+=1
    if d[0]==0:
        #检测是否延时
        delta=d[1]-d[2]
        if delta>5:
            print("delayus(%.2f)" % delta)

        #检查下一高电平时间,SWD从输出切换到输入时会增加延时 r or w
        t = ds[n]
        r = t[1]/d[2]
        if r<1.8:
            func="write_byte"
        elif r<6.5:
            func="read_byte"
        else:
            func="unknown_byte"
            print(t[1], d[2], r, end="")

        #检查是否快速模式
        if d[2]<0.5:
            func += "_fast"


        print("%s(1, " % func, end="")
        while n<dn:
            sd = 0
            for i in range(8):
                sd>>=1
                d = ds[n]
                n+=1
                if d[0]==1:
                    sd |= 0x80
            print("0x%02x, " % sd, end="")

            d = ds[n]
            n+=1
            # 1 end   0 continue
            if d[0]==1:
                print("1)")
                break
            else:
                print("0)")
                print("%s(0, " % func, end="")
    else:
        #2 4 5 8 10 30 40
        idle=1
        func="idle"
        #检查是否快速模式
        if d[2]<0.5:
            func += "_fast"
        while n<dn: 
            d = ds[n]
            if d[0]==0:
                break
            n+=1
            idle+=1
        print("%s(%d)" % (func,idle))






