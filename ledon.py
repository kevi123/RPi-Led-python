#Kevin Hinojosa
#This serves as a simple LED setup for GPIO usage.
#run power from 3.3V
#Use a 220 ohm resister --{red red brown gold}--
# Led long end is +ANode, short is -Cathode
#USE GPIO pin names

import RPi.GPIO as GPIO     #this allows us to use General Purpose Input Output Pins
import time                     #time allows us to use sleep function
GPIO.setmode(GPIO.BCM)      #this tells The pi how to read the pins, GPIO.BCM is titles, GPIO.BOARD is 12 34 56 78 starting at top left
GPIO.setup(18, GPIO.OUT)    #this tells the pi to use this pin as output


counter=0
myBool= True

while counter<=5:
    print("counter is ", counter,".")
    GPIO.output(18, True)       #this sets output to True== 1 or False ==0.
    print("Led On")
    time.sleep(1)               #time is in seconds or milli(.150)

    GPIO.output(18, False)
    print ("Led off")
    time.sleep(1)
    counter=counter+1





GPIO.cleanup() # cleanup all GPIO or we will have warning errors that pins are in use
