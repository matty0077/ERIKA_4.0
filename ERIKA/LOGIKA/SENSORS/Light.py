#!/usr/bin/env python
from rgb_lcd import *
import time
import grovepi

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 1

grovepi.pinMode(light_sensor,"INPUT")

'''while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)


        print("sensor_value = %d " %(sensor_value))
        time.sleep(.5)

    except IOError:
        print ("Error")'''

def LVIS():
    try:
        vis = grovepi.analogRead(light_sensor)#read sensor data
        #print('Vis:             ' + str(vis))
        setText('Visible Light Reading at: ' + str(vis))
        Set_Aqua()
        time.sleep(.75)

        if vis>=0 and vis <30:
                setText("Very Dark")
                Set_Red()
                
        elif vis >=30 and vis<=100:
                setText("A Little Dark")
                Set_Green()

        elif vis >100 and vis<=265:
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
        print ("Light Connection Error")



#while True:
    #LVIS()
    #time.sleep(.75)
