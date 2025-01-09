from machine import Pin, I2C
import utime,uarray

DS3231_address = 0x68
OLEDaddress=  0x3C
command=  0x00
data_cmd=  0x40
Cstart=0
Cend=0
Pstart=0
Pend=0


def read_time():
    buf = bytearray([0x00])
    i2c.writeto(DS3231_address,buf,False)
    time=i2c.readfrom(DS3231_address,3,True)
    BCD = time[0]
    sec1= chr(((BCD & 0xf0) >> 4 ) | 0x30)
    sec0= chr((BCD & 0x0f)  | 0x30)
    BCD = time[1]
    min1= chr(((BCD & 0xf0) >> 4 ) | 0x30)
    min0= chr((BCD & 0x0f)  | 0x30)
    BCD = time[2]
    hour1= chr(((BCD & 0xf0) >> 4 ) | 0x30)
    hour0= chr((BCD & 0x0f)  | 0x30)
    print(hour1,hour0,':',min1,min0,':',sec1,sec0)
    return time

def write_time():
    hour_in= input("input hour 0-23 :  ")
    BCD = hour_in
    
    i = 0
    for x in BCD:
        if i == 0:
            a=int(x)
            i+=1
        else:
            b= int(x)
    a=a<<4
    a= a|b
    hour_in=a
    min_in= input("input min 0-59 :  ")
    BCD = min_in
    
    i = 0
    a=0
    b=0
    for x in BCD:
        if i == 0:
            a=int(x)
            i+=1
        else:
            b= int(x)
    a=a<<4
    a= a|b
    min_in=a
    sec_in=0x00
    #buf = bytearray([0x00,sec_in,min_in,hour_in])
    #i2c.writeto(DS3231_address,buf,False)
    
    day_in= input("input day monday to sunday 0-7 :  ")
    day_in = int(day_in)
    
    date_in= input("input date 1-31 :  ")
    BCD = date_in
    
    i = 0
    a=0
    b=0
    for x in BCD:
        if i == 0:
            a=int(x)
            i+=1
        else:
            b= int(x)
    a=a<<4
    a= a|b
    date_in=a
    
    month_in= input("input month 1-12 :  ")
    BCD = month_in
    
    i = 0
    a=0
    b=0
    for x in BCD:
        if i == 0:
            a=int(x)
            i+=1
        else:
            b= int(x)
    a=a<<4
    a= a|b
    month_in=a
    
    
    year_in= input("input year 0-99 :  ")
    BCD = year_in
    
    i = 0
    a=0
    b=0
    for x in BCD:
        if i == 0:
            a=int(x)
            i+=1
        else:
            b= int(x)
    a=a<<4
    a= a|b
    year_in=a
    buf = bytearray([0x00,sec_in,min_in,hour_in,day_in,date_in,month_in,year_in])
    i2c.writeto(DS3231_address,buf,True)
    
# I2C Initialization
i2c = I2C(id=0,scl=Pin(9),sda=Pin(8),freq=100_000)
write_time()
while True:
    read_time()
    utime.sleep(1)



i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
devices = i2c.scan()