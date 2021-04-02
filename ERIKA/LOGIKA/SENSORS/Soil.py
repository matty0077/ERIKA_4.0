#!/usr/bin/env python
from rgb_lcd import *
import grovepi
import time

#declare sensor slot at A1
mositure_sensor	= 0
        
def Soil():#Reads Soil MOisture and helps Judge appropriate Seeding Locations
        moisture=grovepi.analogRead(mositure_sensor)#Read sensor Data
        setText("Soil Moisture Reading at: " + str(moisture))
        Set_Aqua()
        time.sleep(.75)

        try:
                if moisture<=5:
                    setText("OPen Air. Bad for Planting ")
                    Set_Red()
                        
                elif moisture>5 and self.moisture<=18:
                    setText("Dry Soil. Not Ideal ")
                    Set_Yellow()
                        
                elif moisture>425 and self.moisture<=690:
                    setText("Humid Soil. Ideal")
                    Set_Green()
                        
                elif moisture>690:
                    setText("Submerged. Bad for Planting")
                    Set_Red()

                time.sleep(1)
                Set_Clear()
                
        except KeyboardInterrupt:
                Set_Clear()
                sys.exit()#exits program
        except TypeError:
                print ("Error")
        
        except IOError:
                setText("Soil Connection Error")
                Set_Red()
                time.sleep(1)
                Set_Clear()


#Soil()
