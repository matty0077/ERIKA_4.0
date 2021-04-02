#!/usr/bin/env python

###ERIKA SYSTEM- Manages Environmental Info for any applicable purpose
#SUN-measures visible, ultraviolet and infrared light,skin cancer warnings
#SOIL MOISTURE-self explanetory
#TEMPerature/HUMIDity-calculate temp/humid, dew point, fog and frost
#rgblcd- show you data uses color for more info
#button- for switching modes

import sys
sys.path.append("/home/pi/Desktop/Grove_2.0/LOGIKA/")
sys.path.append('/home/pi/Desktop/Grove_2.0/LOGIKA/SENSORS/')

import threading
import time
import subprocess
import math
import logging
from datetime import datetime

from META import *
from rgb_lcd import *
from Light import *
from Soil import *
from Temp_Humid import *
import grovepi
from grovepi import *

# Connect the Grove Touch Sensor to digital port D3
touch_sensor = 8
grovepi.pinMode(touch_sensor,"INPUT")

######Erika class manages these specific sensors for the purposes of plantingg
class ERIKA:
        MODE=0
        TIME= "%a %-d %b %-I:%M"
########################DATE TIME
        def Date_Time(self):
                msg = "%s" % (datetime.now().strftime(self.TIME))
                setText(msg)
                Set_Yellow()
                time.sleep(1)
                Set_Clear()

################################button
        def Button(self):
                press=grovepi.digitalRead(touch_sensor)
                print(press)
                if press==1:
                        self.MODE+=1
                        if self.MODE>9:
                                self.MODE=0
                                
##############simple scan of environment
        def Quick_Scan(self):
                TEMP()
                time.sleep(1)
                HUMID()
                time.sleep(1)
                Dew_Point()
                time.sleep(1)
                VAPOR()
                time.sleep(1)
                Sun()
                time.sleep(1.5)

#############abbreviate class                
E=ERIKA()

###########MAIN PROGRAM(FOR SWITCHING MODESc)
while True:
    try:
        if  E.MODE==0:#date/time
                E.Date_Time()
                Threader(E.Button)
        elif  E.MODE==1:#temperature
                TEMP()
                Threader(E.Button)
        elif  E.MODE==2:#humidity
                HUMID()
                Threader(E.Button)
        elif  E.MODE==3:#air pressure
                Dew_Point()
                Threader(E.Button)
        elif  E.MODE==4:#Altitude
                VAPOR()
                Threader(E.Button)
        elif  E.MODE==5:#dew point
                VIS()
                Threader(E.Button)
        elif  E.MODE==6:#pesticide effectiveness
                UV_PPL()
                Threader(E.Button)
        elif  E.MODE==7:#water vapor for fog n frost
                UV_AGRI()
                Threader(E.Button)
        elif  E.MODE==8:#IR light for plants
                IR()
                Threader(E.Button)
        elif  E.MODE==9:#soil  moisture
                Soil()
                Threader(E.Button)

    except KeyboardInterrupt:
        Set_Clear()
        break
        sys.exit()
    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
        
