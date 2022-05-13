from machine import I2C
from sh1106 import SH1106_I2C
import machine
import utime
import os

i2c = I2C(0)
oled = SH1106_I2C(128, 64, i2c)
LED_FileWrite = machine.Pin(25,machine.Pin.OUT)
switch  = machine.Pin(0,machine.Pin.IN, machine.Pin.PULL_UP)
switch1 = machine.Pin(1,machine.Pin.IN, machine.Pin.PULL_UP)
switch2 = machine.Pin(2,machine.Pin.IN, machine.Pin.PULL_UP)
switch3 = machine.Pin(3,machine.Pin.IN, machine.Pin.PULL_UP)
a0 = machine.ADC(26)
a1 = machine.ADC(27)
a2 = machine.ADC(28)
LogFileName = "log0.txt"
Log1FileName = "log1.txt"
Log2FileName = "log2.txt"
Max_File_Size = 1000
i=90
arr = [0] * 110
flag = 1
flag1 = 0
flag2 = 0

oled.rotate(180)
oled.text("HELLO EVERYONE",0,20)
oled.text("WELCOME",35,40)
oled.show()
utime.sleep(5)
oled.fill(0)
    
def get_max(arr, n):
    i=0
    max = arr[0]
    #print("n = ",n)
    while(i < n):
        if(arr[i]>max):
            print(".")
            max = arr[i]
        i+=1
    return max
    
def get_min(arr, n):
    i=0
    min = arr[0]
    #print("n = ",n)
    while(i < n-1):
        if(arr[i]<min):
            print(".")
            #print("min : ", min)
            min = arr[i]
        i+=1
    return min
    
def get_data0():
    a=0
    i=0
    sum=0
    while i < 100 :
        a = a0.read_u16()
#         utime.sleep_us(10)
        sum = sum +a
        #print ("sum: ",sum)
        i+=1
    sum = (sum / 100000)
    return sum

def get_data1():
    a=0
    i=0
    sum=0
    while i < 100 :
        a = a1.read_u16()
        sum = sum +a
#         utime.sleep_us(10)
#         print(sum)
        #print ("sum: ",sum)
        i+=1
    sum = (sum / 100000)
    return sum

def get_data2():
    a=0
    i=0
    sum=0
    while i < 100 :
        a = a2.read_u16()
#         utime.sleep_us(10)
        sum = sum +a
        #print ("sum: ",sum)
        i+=1
    sum = (sum / 100000)
    return sum

def WriteFile(passed,m):
    if(m==0):
        LED_FileWrite.value(1) 
        log = open(LogFileName,"a") 
        log.write(passed)
        log.close()
        LED_FileWrite.value(0)
    if(m==1):
        LED_FileWrite.value(1) 
        log1 = open(Log1FileName,"a") 
        log1.write(passed)
        log1.close()
        LED_FileWrite.value(0)
    if(m==2):
        LED_FileWrite.value(1) 
        log2 = open(Log2FileName,"a") 
        log2.write(passed)
        log2.close()
        LED_FileWrite.value(0)

def CheckFileSize(m):
    try:
        if(m == 0):
            f = open(LogFileName,"r") 
            f.seek(0, 2)
            size = f.tell()
            f.close()
            #print("size : ")
            return size
        if(m == 1):
            f1 = open(Log1FileName,"r") 
            f1.seek(0, 2)
            size = f1.tell()
            f1.close()
            #print("size : ")
            return size
        if(m == 2):
            f2 = open(Log2FileName,"r") 
            f2.seek(0, 2)
            size = f2.tell()
            f2.close()
            #print("size : ")
            return size
    except:
        return 0 


def Read(m):
    if(m == 0):
        LED_FileWrite.value(1) 
        tmpName = LogFileName + '.bak'

        with open(LogFileName, 'r') as readFrom:
            a = readFrom.readlines()
            n = len(a)
            i=0
            print("length : ",n)
            oled.fill(0)
            oled.text("data stored: ",0,20)
            oled.text(str(n),50,40)
            utime.sleep(3)
            oled.fill(0)
            while (i < n) :
                arr[i]=a[i]
                print("data ", i+1,"= ", arr[i])
                utime.sleep(0.1)
                i+=1
            #print("a = ",(float(arr[3]))-1)
            #print("length : ",n)
            return arr, n
    if(m == 1):
        LED_FileWrite.value(1) 
        tmpName = Log1FileName + '.bak'

        with open(Log1FileName, 'r') as readFrom:
            a = readFrom.readlines()
            n = len(a)
            i=0
            while (i < n) :
                arr[i]=a[i]
                print("data ", i+1,"= ", arr[i])
                utime.sleep(0.1)
                i+=1
            #print("a = ",(float(arr[3]))-1)
            #print("length : ",n)
            return arr, n
    if(m == 2):
        LED_FileWrite.value(1) 
        tmpName = Log2FileName + '.bak'

        with open(Log2FileName, 'r') as readFrom:
            a = readFrom.readlines()
            n = len(a)
            i=0
            while (i < n) :
                arr[i]=a[i]
                print("data ", i+1,"= ", arr[i])
                utime.sleep(0.1)
                i+=1
            #print("a = ",(float(arr[3]))-1)
            #print("length : ",n)
            return arr, n

def string_size(flag,m):
    print("flag : ",flag)
    if(flag == 0 ):
        return 0
    else:
        if(m == 0):
            LED_FileWrite.value(1) 
            tmpName = LogFileName + '.bak'

            with open(LogFileName, 'r') as readFrom:
                a = readFrom.readlines()
                n = len(a)
            return n
        if(m == 1):
            LED_FileWrite.value(1) 
            tmpName = Log1FileName + '.bak'

            with open(Log1FileName, 'r') as readFrom:
                a = readFrom.readlines()
                n = len(a)
            return n
        if(m == 2):
            LED_FileWrite.value(1) 
            tmpName = Log2FileName + '.bak'

            with open(Log2FileName, 'r') as readFrom:
                a = readFrom.readlines()
                n = len(a)
            return n

while True:
    utime.sleep(0.1)
    print("switch : ",switch.value())
    print("switch1 : ",switch1.value())
    print("switch2 : ",switch2.value())
    print("switch3 : ",switch3.value())
    if(switch.value()==0):
        if (flag1 == 1):
            oled.fill(0)
            oled.text("please sterlize",0,20)
            oled.text("THE NOZZLE",20,40)
            oled.show()
            utime.sleep(2)
            oled.fill(0)
        else:
            if(CheckFileSize(0) < Max_File_Size) :
                stringToWrite = str(get_data0()) + "\r\n"
                WriteFile(stringToWrite,0)
                print("writing..............")
                oled.text("writting0", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting0.", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting0..", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting0...", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting0....", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.fill(0)
            else:
                print("storage 0 full")
                oled.text("storage 0 full", 5, 30)
                oled.show()
                utime.sleep(1)
                oled.fill(0)
            if(CheckFileSize(1) < Max_File_Size) :
                stringToWrite1 = str(get_data1()) + "\r\n"
                WriteFile(stringToWrite1,1)
                print("writing..............")
                oled.fill(0)
                oled.text("writting1", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting1.", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting1..", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting1...", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting1....", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.fill(0)
            else:
                print("storage 1 full")
                oled.text("storage 1 full", 5, 30)
                oled.show()
                utime.sleep(1)
                oled.fill(0)
            if(CheckFileSize(2) < Max_File_Size) :
                stringToWrite2 = str(get_data2()) + "\r\n"
                WriteFile(stringToWrite2,2)
                print("writing..............")
                oled.fill(0)
                oled.text("writting2", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting2.", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting2..", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting2...", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.text("writting2....", 5, 30)
                oled.show()
                utime.sleep(0.1)
                oled.fill(0)
            else:
                print("storage 2 full")
                oled.text("storage 2 full", 5, 30)
                oled.show()
                utime.sleep(1)
                oled.fill(0)
            oled.text("Data updated", 5, 30)
            oled.show()
            utime.sleep(1)
            oled.fill(0)
            flag1 = 1

    if(switch1.value()==0):
#         utime.sleep(1)
#         print("flag: ",flag)
        a = string_size(flag,0)
        oled.fill(0)
        oled.text("stored data: ",0,30)
        oled.text(str(a),110,30)
        oled.show()
#         print("....................................",a)
        utime.sleep(3)
        oled.fill(0)
        oled.text("calculating ....", 0, 0)
        oled.show()
        utime.sleep(1)
        Read(0)
        n = len(arr)
        arr1 = map(float,arr)
        arr2 = list(arr1)
        max = get_max(arr2, n)
        min = get_min(arr2, n)
        print("max0 : ",max)
        print("min0 : ",min)
        oled.text("max0: ", 0, 0)
        oled.text(str(max), 50, 0)
        oled.text("min0: ", 0, 10)
        oled.text(str(min), 50, 10)
        oled.show()
        utime.sleep(0.1)
        print("-----------------------------------------------------")
        oled.show()
        Read(1)
        n = len(arr)
        arr1 = map(float,arr)
        arr2 = list(arr1)
        max = get_max(arr2, n)
        min = get_min(arr2, n)
        print("max1 : ",max)
        print("min1 : ",min)
        oled.text("max1: ", 0, 22)
        oled.text(str(max), 50, 22)
        oled.text("min1: ", 0, 32)
        oled.text(str(min), 50, 32)
        oled.show()
        print("-----------------------------------------------------")
        Read(2)
        n = len(arr)
        arr1 = map(float,arr)
        arr2 = list(arr1)
        max = get_max(arr2, n)
        min = get_min(arr2, n)
        print("max2: ",max)
        print("min2: ",min)
        oled.text("max2: ", 0, 44)
        oled.text(str(max), 50, 44)
        oled.text("min2: ", 0, 54)
        oled.text(str(min), 50, 54)
        oled.show()
        print("-----------------------------------------------------")
        utime.sleep(10)
        oled.fill(0)
    if(switch2.value()==0):
        size = string_size(flag,0)
        print("size 0: ",size)
        size = string_size(flag,1)
        print("size 1: ",size)
        size = string_size(flag,2)
        print("size 2: ",size)
        utime.sleep(2)
        if(switch2.value()==0):
            f = open('log0.txt', 'w')
            os.remove('log0.txt')
            f1 = open('log1.txt', 'w')
            os.remove('log1.txt')
            f2 = open('log2.txt', 'w')
            os.remove('log2.txt')
            flag = 0
            print("cleared..........................")
            oled.text("data cleared...", 5, 30)
            oled.show()
            utime.sleep(1)
            oled.fill(0)
            oled.text("..........")
            oled.show()
    if (switch3.value() == 0):
        if (flag1 == 1):
            oled.fill(0)
            oled.text("please sterlize",0,20)
            oled.text("THE NOZZLE",20,40)
            oled.show()
            utime.sleep(2)
            oled.fill(0)
        else:
            data0 = get_data0()
            print("data0: ",data0)
            oled.fill(0)
            oled.text("data0: ", 0, 0)
            oled.text(str(data0), 50, 0)
            oled.show()
            data1 = get_data1()
            print("data1: ",data1)
            oled.text("data1: ", 0, 20)
            oled.text(str(data1), 50, 20)
            oled.show()
            data2 = get_data2()
            print("data2: ",data2)
            oled.text("data2: ", 0, 40)
            oled.text(str(data2), 50, 40)
            oled.show()
            utime.sleep(5)
            flag1 = 1
            Read(0)
            n = len(arr)
            arr1 = map(float,arr)
            arr2 = list(arr1)
            max0 = get_max(arr2, n)
            min0 = get_min(arr2, n)
            print("max0 : ",max0)
            print("min0 : ",min0)
            Read(1)
            n = len(arr)
            arr1 = map(float,arr)
            arr2 = list(arr1)
            max1 = get_max(arr2, n)
            min1 = get_min(arr2, n)
            print("max1 : ",max1)
            print("min1 : ",min1)
            Read(2)
            n = len(arr)
            arr1 = map(float,arr)
            arr2 = list(arr1)
            max2 = get_max(arr2, n)
            min2 = get_min(arr2, n)
            print("max2: ",max2)
            print("min2: ",min2)
            if(max0 > data0 > min0 ):
                print("1........")
                flag2+=1
            if(max1 > data1 > min1 ):
                print("2........")
                flag2+=1
            if(max2 > data2 > min2 ):
                print("3........")
                flag2+=1
            print("flag2 : ",flag2)
            if(flag2 == 0):
                print("NEGATIVE...")
                oled.fill(0)
                oled.text("NEGATIVE...", 0, 30)
                oled.show()
                utime.sleep(5)
            if(flag2 == 1):
                print("POSITIVE...1")
                oled.fill(0)
                oled.text("POSITIVE...", 0, 20)
                oled.text("Risk .", 0, 40)
                oled.text("Level'", 0, 50)
                oled.text("LOW", 50, 45)
                oled.show()
                utime.sleep(5)
            if(flag2 == 2):
                print("POSITIVE...2")
                oled.fill(0)
                oled.text("POSITIVE...", 0, 20)
                oled.text("Risk .", 0, 40)
                oled.text("Level'", 0, 50)
                oled.text("MODERATE", 50, 45)
                oled.show()
                utime.sleep(5)
            if(flag == 3):
                print("POSITIVE...3")
                oled.fill(0)
                oled.text("POSITIVE...", 0, 20)
                oled.text("Risk .", 0, 40)
                oled.text("Level'", 0, 50)
                oled.text("HIGH", 50, 45)
                oled.show()
                utime.sleep(5)
        

