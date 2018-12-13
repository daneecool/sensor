import RPi.GPIO as GPIO
import time
import signal

GPIO.setmode(GPIO.BCM)

# Define Pins
LEDG_PIN_VIN = 18
LEDR_PIN_VIN = 12
MAGNETICDOORSWITCH3V3_PIN_SIG = 4
PUSHBUTTON_PIN = 17
PULLPUSHSOLENOID_PIN_SIG = 13

# Initially we don't know if the door sensor is open or closed...
isOpen = None
aldOpen = None

# Set up the light pins.
GPIO.setup(LEDR_PIN_VIN , GPIO.OUT)
GPIO.setup(LEDG_PIN_VIN , GPIO.OUT)

# Set up solenoid
GPIO.setup(PULLPUSHSOLENOID_PIN_SIG , GPIO.OUT , initial=GPIO.LOW)

# Set up the door sensor pin + pushbutton 
GPIO.setup(MAGNETICDOORSWITCH3V3_PIN_SIG , GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PUSHBUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up the light pins.
GPIO.setup(LEDR_PIN_VIN , GPIO.OUT)
GPIO.setup(LEDG_PIN_VIN , GPIO.OUT) 

# Make sure all lights are off.
GPIO.output(LEDR_PIN_VIN , False)
GPIO.output(LEDG_PIN_VIN , False)

def cleanupLights(signal, frame): 
    GPIO.output(LEDR_PIN_VIN, False) 
    GPIO.output(LEDG_PIN_VIN, False)  
    GPIO.cleanup() 
    sys.exit(0)

# Set the cleanup handler for when user hits Ctrl-C to exit
signal.signal(signal.SIGINT, cleanupLights)

while True:
    input_state = GPIO.input(PUSHBUTTON_PIN) 
    if (input_state == False):
        aldOpen = isOpen
        isOpen = GPIO.input(MAGNETICDOORSWITCH3V3_PIN_SIG)
        if (isOpen and (isOpen != aldOpen)):
            GPIO.output(PULLPUSHSOLENOID_PIN_SIG , False)
            GPIO.output(LEDG_PIN_VIN , False)
            GPIO.output(LEDR_PIN_VIN , True)
            print ("Door is LOCK")
        elif (isOpen != aldOpen):
            GPIO.output(PULLPUSHSOLENOID_PIN_SIG , True)
            GPIO.output(LEDR_PIN_VIN , False)
            GPIO.output(LEDG_PIN_VIN , True)
            print ("Door is UNLOCK")
    elif (input_state == True):
        print("EXIT")
        GPIO.output(PULLPUSHSOLENOID_PIN_SIG , True)
        GPIO.output(LEDG_PIN_VIN , True)
        GPIO.output(LEDR_PIN_VIN , False)
time.sleep(3)
