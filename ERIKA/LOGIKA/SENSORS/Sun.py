#!/usr/bin/env python

#create direct paths to streamline the importing process
import sys
sys.path.append('/home/pi/Desktop/Grove_2.0/ERIKA/LOGIKA/SENSORS/SPECS/')

#import necessities
import time
from rgb_lcd import *
import grovepi

#suni2c
import SI1145
sensor = SI1145.SI1145()

###################################INFRARED DATA-vital for stem growth SPEED and plant SIZE.
#too much infrared and the plants are bigger but weaker. too little infrared, your plant is smaller but denser
def IR():#VALUES NEED WORK
    try:
        IR = sensor.readIR()#read sensor data
        #print('IR:              ' + str(IR))
        setText('InfraRed Reading at: ' + str(IR) + " LM")
        Set_Aqua()
        time.sleep(.75)
        
        if IR <=500:#low uv
                setText("Low Infrared for Plants")
                Set_Red()

        elif IR >500 and IR<=710:#ideal uv
                setText("Ideal Infrared for Plant Growth")
                Set_Green()
                
        elif IR>710:#high uv
                setText("Moderately High IR for Plants")
                Set_Yellow()
                time.sleep(1)
                setText("Higher Risk of Overexposure. Not Recommended")

        time.sleep(1)
        Set_Clear()
    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()#exits program
    except TypeError:
        print ("Error")
    except IOError:
        print ("Sun Connection Error")
    
##########################VISIBLE LIGHT-vital for photosynthesis(plant food)
def VIS():
    try:
        vis = sensor.readVisible()#read sensor data
        #print('Vis:             ' + str(vis))
        setText('Visible Light Reading at: ' + str(vis) + " LM")
        Set_Aqua()
        time.sleep(.75)

        if vis>=0 and vis <30:
                setText("Very Dark")
                Set_Red()
                
        elif vis >=30 and vis<=265:
                setText("Decently Lit")
                Set_Green()
                
        elif vis>265 and vis < 500:
                setText("very well Lit")
                Set_Green()
                
        elif vis>500:
                setText("Very, Very Bright Environment")
                Set_Yellow()

        time.sleep(1)
        Set_Clear()
    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()#exits program
    except TypeError:
        print ("Error")
    except IOError:
        print ("Sun Connection Error")

############################UV STATS FOR Typical Agriculture
def UV_AGRI():#VALUES NEED WORK
    try:
        UV = sensor.readUV()#read sensor data
        #print('UV:        ' + str(UV))
        setText('Ultraviolet Reading at: ' + str(UV))
        Set_Aqua()
        time.sleep(.75)
        
        if UV>=0 and UV <=2:
                setText("low uv for plants")
                Set_Red()
                
        elif UV >2 and UV<=5:
                setText("ideal uv for planting")
                Set_Green()
                
        elif UV>5 and UV <=7:
                setText("moderately high uv for plants")
                Set_Yellow()
                time.sleep(.75)
                setText("careful not to overexpose plants")
                
        elif UV>7 and UV<=10:
                setText("HIGH uv for plants")
                Set_Yellow()
                time.sleep(.75)
                setText("Not Totally Recomended")
                
        elif UV>10:
                setText("Dangerous UV Radiation for typical planting")
                Set_Red()
                
        time.sleep(1)
        Set_Clear()

    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()#exits program
    except TypeError:
        print ("Error")
    except IOError:
        print ("Sun Connection Error")
        
##########################UV Safety FOR PEOPLE BASED ON THE UVI VALUES SET BY THE WORLD HEALTH ORGANIZATION  
def UV_PPL():
    try:
        UV = sensor.readUV()
        uvIndex = UV / 100.0#converts raw UV to UVI chart
        #print('UV Index:        ' + str(uvIndex))
        setText('UVI Reading at: ' + str(uvIndex))
        Set_Aqua()
        time.sleep(.75)

        ###make one for 0
        if uvIndex<1:
                setText("Negligable UV Danger")
                Set_Green()
                
        if uvIndex>=1 and uvIndex <=2:
                setText("low UV risk to skin")
                Set_Green()

        elif uvIndex >2 and uvIndex<=5:
                setText("Moderate UV risk to skin")
                Set_Green()
                
        elif uvIndex>5 and uvIndex <=7:
                setText("High UV risk to skin")
                Set_Yellow()
                
        elif uvIndex>7 and uvIndex<=10:
                setText("Danerous Ultraviolet Radiation")
                Set_Yellow()#orange
                
        elif uvIndex>10:
                setText("Extremely Danerous Ultraviolet Radiation")
                Set_Red()
                
        time.sleep(1)
        Set_Clear()

    except KeyboardInterrupt:
        Set_Clear()
        sys.exit()#exits program
    except TypeError:
        print ("Error")
    except IOError:
        print ("Sun Connection Error")
    
##########################TESTS
#UV_PPL()
#IR()
#VIS()
'''while True:
    IR()
    time.sleep(.75)
    VIS()
    time.sleep(.75)
    UV_AGRI()
    time.sleep(.75)
    UV_PPL()'''
                
