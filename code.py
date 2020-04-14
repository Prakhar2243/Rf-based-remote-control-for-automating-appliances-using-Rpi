import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
#GPIO.setwarinigs(False)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
status=0
flag =0
flag1=0
while True:


if(GPIO.input(21) == False):

 GPIO.output(26,1)


 print("Light On")
 time.sleep(1)
 else :
 GPIO.output(26,0)


 print("Light Off")
 time.sleep(1)
 if(GPIO.input(20) == False):



 GPIO.output(19,1)


 print"Fan On"
 time.sleep(1)
 else:
 GPIO.output(19,0)


 print"Fan Off"
 time.sleep(1)
if(GPIO.input(16) == False):


 GPIO.output(13,1)

 else:


 GPIO.output(13,0)
 if(GPIO.input(12) == False):

 GPIO.output(6,1)
 else:

 GPIO.output(6,0)
time.sleep(0.2)
GPIO.cleanup()
