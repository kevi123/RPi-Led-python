import RPi.GPIO as GPIO     #this allows us to use General Purpose Input Output Pins
import time                     #time allows us to use sleep function
GPIO.setmode(GPIO.BCM)      #this tells The pi how to read the pins, GPIO.BCM is titles, GPIO.BOARD is 12 34 56 78 starting at top left
GPIO.setup(18, GPIO.OUT)    #this tells the pi to use this pin as output




GPIO.output(18, True)       #this sets output to True== 1 or False ==0.
print("Led On")
time.sleep(1)



GPIO.output(18, False)
time.sleep(1)
print ("Led off")

GPIO.output(18, True)
print("Led On")
time.sleep(1)

GPIO.output(18, False)
print("led off")
time.sleep(1)

GPIO.output(18, True)
print("Led On")
time.sleep(1)

GPIO.cleanup() # cleanup all GPIO or we will have warning errors that pins are in use
