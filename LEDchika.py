#!/usr/bin/python
#coding: utf-8;
#

import  RPi.GPIO as GPIO
import time
RED=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED,GPIO.OUT)
while True:
	GPIO.output(RED,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(RED,GPIO.LOW)
	time.sleep(0.5)
