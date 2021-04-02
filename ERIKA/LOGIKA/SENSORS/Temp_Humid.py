from rgb_lcd import *
import time
from grovepi import *

dht_sensor_port = 2		# Connect the DHt sensor to port d2
dht_sensor_type = 0             # change this depending on your sensor type - see header commentwhile True:

######################################TEMPERATURE(Celsius and Farhenheit)              
def TEMP():
        try:
                #########sensor readings
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                #########calculate temperature for farenheight(Celsius is Default)
                tempF=temp*1.8+32
                tempF = round(tempF)
                tempF = int(tempF)
                #Display Temperature as F AND C
                setText("Temperature " + str(tempF) +"F" + "/" + str(temp) +"C")
                Set_Aqua()
                time.sleep(.75)
                
                ########info(customize Info for celsius if needed)
                if tempF<=50:
                    setText("Little Chilly")
                    Set_Yellow()

                elif tempF>55 and tempF<=70:
                    setText("Ideal Temperature")
                    Set_Green()

                elif tempF>70:
                    setText("A Little Hot")
                    Set_Green()
                    
                time.sleep(1) 
                Set_Clear()
			
        except (IOError,TypeError) as e:
                setText("Temperature Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()

###############################################HUMIDITY
def HUMID():
        try:
                #########sensor readings
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                #Display Humidity %
                setText("Humidity " + str(hum) + "%")
                Set_Aqua()
                time.sleep(.75)

                ########info
                if hum<30:
                    setText("Somewhat Dry")
                    Set_Yellow()

                elif hum>=30 and hum<=60:
                    setText("Ideal Humidity")
                    Set_Green()

                elif hum>60 and hum<80:
                    setText("Moderate Humidity")
                    Set_Green()

                else:
                    setText("High Humidity")
                    Set_Green()
                    
                time.sleep(1)
                Set_Clear()
			
        except (IOError,TypeError) as e:
                setText("Humidity Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()
                
###################################CALCULATES DEW POINT
def Dew_Point():
        try:
                #sensor Reading
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                DEW = temp-(14.55+0.114*temp)*(1-(0.01*hum))-((2.5+0.007*temp)*(1-(0.01*hum)))**3-(15.9+0.117*temp)*(1-(0.01*hum))**14
                DEW = round(DEW)
                DEW = int(DEW)
                #DEW=temp-((100-hum)/5)#Simple dewpoint model by mark g. lawrence
                #Display Dew Point
                setText("DewPoint Humidity at: "+str(DEW))
                Set_Aqua()
                time.sleep(.75)
                
                if DEW>=24:
                        setText("High Dewpoint Humidity")
                        Set_Aqua()
                        
                elif DEW >= 16 and DEW < 24:
                        setText("Moderate Dewpoint Humidity")
                        Set_Aqua()

                elif DEW >= 10 and DEW < 16:
                        setText("Moderately Low Dewpoint Humidity")
                        Set_Aqua()
                        
                elif DEW <10:
                        setText("Dry Dewpoint")
                        Set_Aqua()

                time.sleep(1)
                Set_Clear()
			
        except (IOError,TypeError) as e:
                setText("DewPoint Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()

###################################CALCULATES WATER VAPOR for FOG-FROST Readings
def VAPOR():
        try:
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                DEW = temp-(14.55+0.114*temp)*(1-(0.01*hum))-((2.5+0.007*temp)*(1-(0.01*hum)))**3-(15.9+0.117*temp)*(1-(0.01*hum))**14
                DEW = round(DEW)
                DEW = int(DEW)
                
                # Calculate the difference between dew point & current temp
                VAPE = temp - DEW
                VAPE = round(VAPE)
                VAPE = int(VAPE)
                
                #Display Vapor Levels
                setText("Water Vapor at: "+str(VAPE))
                Set_Aqua()
                time.sleep(.75)
                
                if VAPE<=2:
                        setText("Foggy")
                        Set_Aqua()
                        
                elif VAPE >3 and VAPE <=6:
                        setText("Possible Fog")
                        Set_Aqua()

                else:
                        setText("Not Foggy")
                        Set_Aqua()
                        
                # Frost point warning-Uses dewpoint and temperature(celsius)
                if DEW <= 2 and temp <= 1:
                        setText("Frost Warning")
                        Set_Red()

                time.sleep(1)
                Set_Clear()
			
        except (IOError,TypeError) as e:
                setText("Vapor Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()


Dew_Point()
#time.sleep(1)
#VAPOR()
#time.sleep(1)
#TEMP()
#time.sleep(1)
#HUMID()
