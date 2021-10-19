#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import json
import time

ledPins = [16 20 21]
pwmobjects = [led1 led2 led3]

gpio.setmode(GPIO.BCM)
for i in range(2):
  gpio.setup(ledPins[i], GPIO.OUT)
  pwmobjects[i] = GPIO.PWM(ledPin[i], 100) # PWM object on our pin at 100 Hz
  pwmobjects[i].start(0) # start with LED off

while True:
  with open("lab4.txt", 'r') as file:
    leddutycycles = json.load(f) # read duty cycle values from file
    led1.ChangeDutyCycle(long(leddutycycles['green']))
    led2.ChangeDutyCycle(long(leddutycycles['blue']))
    led3.ChangeDutyCycle(long(leddutycycles['red']))
  time.sleep(0.1)
  except KeyboardInterrupt:
    print("Interrupted")

for i in range(2):
  pwmobjects[i].stop()
GPIO.cleanup()