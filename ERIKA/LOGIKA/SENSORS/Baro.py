#
# Measure temperature(F), humidity(%), pressure(hPa) from Grove BME280 every 1 second.
# This code works only for Raspberry pi.
#
# Written by Junghoon Jang
# E-mail: jh95kr2003@gmail.com
#
import sys
sys.path.append('/home/pi/Desktop/Grove_2.0/ERIKA/LOGIKA/SENSORS/SPECS')


import grove_bme280
import sys, time
from rgb_lcd import *

bme280 = grove_bme280.BME280()

#while True :
####################quick scan
def Baro_Scan():
	data = bme280.getAll()
	print("Temperature: %.2fF, Humidity: %.2f%%, Pressure: %.2fhPa" %(data['T'] * 9 / 5 + 32, data['H'], data['P']))

####################Temperature
def Temperature():
    try:
            temp=bme280.getTemperature()
            temp = round(temp)
            temp = int(temp)
            #print("Temperature: %.2fF" %(temp* 9 / 5 + 32) + "/" + " %.2fC" %(temp))
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

            elif tempF>70 and tempF<85:
                setText("A Little warm")
                Set_Green()

            elif tempF>=85:
                setText("Pretty Hot")
                Set_Green()
                    
            time.sleep(1) 
            Set_Clear()
			
    except (IOError,TypeError) as e:
        setText("Temperature Error")
        Set_Red()
        time.sleep(1)
        Set_Clear()
####################Humidity
def Humidity():
    try:
        hum=bme280.getHumidity()
        hum = round(hum)
        hum = int(hum)
        #print("Humidity: %.2f%%" %(hum))
        ##########Display Humidity %
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

####################air Pressure
def Pressure():
        try:
            p=bme280.getPressure()
            p = round(p)
            p = int(p)

            setText("Pressure: %.2fhPa" %(p))
            Set_Aqua()
            time.sleep(.75)

            if p >= 960 and p < 990:
                setText("baro very low %smb (Stormy) -" % (p))
                Set_Aqua()
                
            elif p >= 990 and p < 1000:
                setText("baro low %smb (Rainy) -" % (p))
                Set_Aqua()

            elif p >= 1000 and p < 1015:
                setText("baro mid %smb (Mostly Clear) -" % (p))
                Set_Aqua()
                
            elif p >= 1015 and p < 1030:
                setText("baro high %smb (Clear Skies) -" % (p))
                Set_Aqua()
                
            elif p >= 1030:
                setText("baro very high %smb (Dry Skies) -" % (p))
                Set_Aqua()
                
            time.sleep(1)
            Set_Clear()
            
        except (IOError,TypeError) as e:
            setText("Pressure Error")
            Set_Red()
            time.sleep(1)
            Set_Clear()
##################altitude
def computeHeight():
        try:
            pressure=bme280.getPressure()
            ##calculate Altitude
            Alt=44330.8 * (1 - pow(pressure / 1013.25, 0.190263))
            Alt = round(Alt)
            Alt = int(Alt)
            setText("Altitude:" + str(Alt) + "feet above sea level")
            Set_Teal()
            #return 44330.8 * (1 - pow(pressure / 1013.25, 0.190263));

            time.sleep(1)
            Set_Clear()
            
        except (IOError,TypeError) as e:
            setText("Altitude Error")
            Set_Red()
            time.sleep(1)
            Set_Clear()
####################dew point
def Dew_Point():
    try:
        #sensor Reading
        temp=bme280.getTemperature()
        hum=bme280.getHumidity()
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
        
#################################pesticide efectiveness/Wet Bulb Temperature
def PESTICIDE():
        try:
            temp=bme280.getTemperature()
            hum=bme280.getHumidity()
            p=bme280.getPressure()

            # Wet Bulb Temperature
            Tdc = ((temp-(14.55+0.114*temp)*(1-(0.01*hum))-((2.5+0.007*temp)*(1-(0.01*hum)))**3-(15.9+0.117*temp)*(1-(0.01*hum))**14))
            E = (6.11*10**(7.5*Tdc/(237.7+Tdc)))
            WBc = (((0.00066*p)*temp)+((4098*E)/((Tdc+237.7)**2)*Tdc))/((0.00066*p)+(4098*E)/((Tdc+237.7)**2))
            #print("Wet Bulb Temp:"+str(WBc)+" Celsius")

            ###Delta-T - for the magic number
            ###If the Delta T is between 2C and 8C, pesticides are more effective
            Dt = temp - WBc# in celsius
            DtF = (temp* 9 / 5 + 32) - WBc#in farhenheight(not certain if it works the same as celsius)
            Dt = round(Dt)
            Dt = int(Dt)

            setText("delta-t %sC" % (Dt))
            Set_Olive()
            time.sleep(.75)
            
            if Dt>=2 and Dt<=8:
                setText('Area is pesticide effective')
            elif Dt<2:
                setText('Area is pesticide resistant')


            time.sleep(1)
            Set_Clear()
			
        except (IOError,TypeError) as e:
            setText("Pesticide Error")
            Set_Red()
            time.sleep(1)
            Set_Clear()

###########################Vapor Pressure/Evaporation Rate
def Evap_Rate():
    # Vapor Pressure(Mb)
    try:
            temp=bme280.getTemperature()
            hum=bme280.getHumidity()
            Vp = (6.11*10**(7.5*((temp-(14.55+0.114*temp)*(1-(0.01*hum))-((2.5+0.007*temp)*(1-(0.01*hum)))**3-(15.9+0.117*temp)*(1-(0.01*hum))**14))/(237.7+((temp-(14.55+0.114*temp)*(1-(0.01*hum))-((2.5+0.007*temp)*(1-(0.01*hum)))**3-(15.9+0.117*temp)*(1-(0.01*hum))**14)))))
            Vp = round(Vp)
            Vp = int(Vp)
            
            setText("Vapor Pressure: %sMb -" % (str(Vp)))
            Set_Aqua()

            time.sleep(1)
            Set_Clear()
			
    except (IOError,TypeError) as e:
            setText("Vapor Error")
            Set_Red()
            time.sleep(1)
            Set_Clear()

###################################CALCULATES WATER VAPOR for FOG-FROST Readings
def VAPOR():
        try:
                #sensor Reading
                temp=bme280.getTemperature()
                hum=bme280.getHumidity()
                DEW = temp-(14.55+0.114*temp)*(1-(0.01*hum))-((2.5+0.007*temp)*(1-(0.01*hum)))**3-(15.9+0.117*temp)*(1-(0.01*hum))**14
                DEW = round(DEW)
                DEW = int(DEW)
                
                # Calculate the difference between dew point & current temp
                VAPE = temp - DEW
                VAPE = round(VAPE)
                VAPE = int(VAPE)
                
                #Display Vapor Levels
                setText("Water Vapor at: "+str(VAPE)+"%")
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


#Dew_Point()
#Temperature()
#Humidity()
#Pressure()
#computeHeight()
#PESTICIDE()
#Evap_Rate()
#VAPOR()
#Baro_Scan()
