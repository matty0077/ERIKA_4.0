#!/usr/bin/env python

import time,sys
import random

if sys.platform == 'uwp':
    import winrt_smbus as smbus
    bus = smbus.SMBus(1)
else:
    import smbus
    import RPi.GPIO as GPIO
    rev = GPIO.RPI_REVISION
    if rev == 2 or rev == 3:
        bus = smbus.SMBus(1)
    else:
        bus = smbus.SMBus(0)

# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e #was=3e

# set backlight to (R,G,B) (values from 0..255 for each)
def setRGB(r,g,b):
    bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
    bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
    bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
    bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

# send command to display (no need for external use)    
def textCommand(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

# set display text \n for second line(or auto wrap)     
def setText(text):
    textCommand(0x01) # clear display
    time.sleep(.05)
    textCommand(0x08 | 0x04) # display on, no cursor
    textCommand(0x28) # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

#Update the display without erasing the display
def setText_norefresh(text):
    textCommand(0x02) # return home
    time.sleep(.05)
	
    textCommand(0x08 | 0x04) # display on, no cursor
    textCommand(0x28) # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
		
# example code
def Set_Red():
    for c in range(0,255):
        setRGB(255,255-c,255-c)
        time.sleep(.001)

def Set_Yellow():
    for c in range(0,255):
        setRGB(255,255,255-c)
        time.sleep(.001)

def Set_Green():
    for c in range(0,255):
        setRGB(255-c,255,255-c)
        time.sleep(.001)

def Set_Aqua():
    for c in range(0,255):
        setRGB(255-c,255,255)
        time.sleep(.001)

def Set_Clear():
    for c in range(0,255):
        textCommand(0x01) # clear display
        setRGB(0,0,0)
        time.sleep(.001)
        
def Rando():
    for i in range(0,51):
        setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        time.sleep(.02)

def Set_Blue():
    for c in range(0,255):
        setRGB(255-c,255-c,255)
        time.sleep(.001)

def Set_Pink():
    for c in range(0,255):
        setRGB(255,255-c,255)
        time.sleep(.001)

def Hot_Pink():
    for c in range(0,255):
        setRGB(255,255-c,555-c)
        time.sleep(.001)

def Set_Gray():
    for c in range(0,255):
        setRGB(255,255,255)
        time.sleep(.001)

def Set_Orange():
    for c in range(0,255):
        setRGB(255,55-c,255-c)
        time.sleep(.001)

def Set_Olive():
    for c in range(0,255):
        setRGB(55-c,55-c,255-c)
        time.sleep(.001)

def Set_Purple():
    for c in range(0,255):
        setRGB(55,255-c,55-c)
        time.sleep(.001)

def Set_Teal():
    for c in range(0,255):
        setRGB(55-c,255,55)
        time.sleep(.001)

def Set_AquaGreen():
    for c in range(0,255):
        setRGB(55,255,55-c)
        time.sleep(.001)

#########test func        
'''def Set_Set():
    for c in range(0,255):
        setRGB(55,255,55-c)
        time.sleep(.001)'''
        
#Set_Set()
#time.sleep(1)
#Set_Pink()
#Set_Orange()
#set_red()
#Set_Yellow()
#Set_Green()
#Rando()
#Set_Clear()

