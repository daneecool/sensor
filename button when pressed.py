import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LEDG_PIN_VIN = 18
LEDR_PIN_VIN = 12
PUSHBUTTON_PIN = 17

GPIO.setup(PUSHBUTTON_PIN , GPIO.IN)
GPIO.setup(LEDG_PIN_VIN , GPIO.OUT)
GPIO.setup(LEDR_PIN_VIN , GPIO.OUT)

ButtonState=False # indicate LED is initially 
ButtonState=True  # indicate LED is initially on

while True:
    print(GPIO.input(PUSHBUTTON_PIN))    
    if GPIO.input(PUSHBUTTON_PIN)==1: # button is pressed
            print("door unlocked")
            if ButtonState==False:
                GPIO.output(LEDG_PIN_VIN , True)
                ButtonState=True
                time.sleep(1)
            elif ButtonState==True:
                GPIO.output(LEDG_PIN_VIN , False)
                ButtonState=False
                GPIO.output(LEDR_PIN_VIN , True)
                time.sleep(1)
    elif GPIO.input(PUSHBUTTON_PIN)==0: # button is not pressed
                print("door lock")
                GPIO.output(LEDR_PIN_VIN , True)
                ButtonState=True
                time.sleep(1)
                 
                 