import time
import threading
import pygame

FXPATH="/home/pi/Desktop/Grove_2.0/ERIKA/LOGIKA/FX/"
#//////////////////////threader
def Threader(action):
    THREAD=threading.Thread(target=action)
    #Thread.daemon=True
    THREAD.start()
    THREAD.join()#optional?
    
#////////////////////////////////soundfx
def soundplay(folder, fx, vol):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(vol)#put above?
    pygame.mixer.music.load(FXPATH + folder +'/' + fx + ".wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy==True:
        continue

######################SHUTDOWN MACHINE
def ShutDown():
    import os
    soundplay("meta","shut_off",.7)
    time.sleep(1)
    os.system("sudo shutdown now -P")

########################DATE TIME
def Date_Time():
        import logging
        from datetime import datetime

        # Display the date and time
        dateString = "%a %-d %b %-I:%M"
        msg = "%s" % (datetime.now().strftime(dateString))
        print(msg)


#Date_Time()
#soundplay("misc","upgrade",1.0)
#time.sleep(1)
#soundplay("misc","xdie",.2)
