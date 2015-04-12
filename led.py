import time
import RPi.GPIO as GPIO
import sys 

# the red led cathode is wired to pin 22 of the expansion header
# the yellow led cathode is wired to pin 18 of the expansion header
# the green led cathode is wired to pin 16 of the expansion header
REDLED = 22
YELLOWLED = 18
GREENLED = 16

# set up control for the channel and pull to a known state
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(REDLED, GPIO.OUT)
GPIO.output(REDLED, GPIO.LOW)
GPIO.setup(YELLOWLED, GPIO.OUT)
GPIO.output(YELLOWLED, GPIO.LOW)
GPIO.setup(GREENLED, GPIO.OUT)
GPIO.output(GREENLED, GPIO.LOW)

# expect to be invoked as led.py {red|yellow|green}
# with no arguments defaults to turning off all led
if len(sys.argv) == 2:
        if sys.argv[1] == "red":
		GPIO.output(REDLED, GPIO.HIGH)
	if sys.argv[1] == "yellow":	
		GPIO.output(YELLOWLED, GPIO.HIGH)
	if sys.argv[1] == "green":	
		GPIO.output(GREENLED, GPIO.HIGH)
