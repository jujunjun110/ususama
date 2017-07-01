#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time

room1 = {'pin': 18, 'status': 0, 'history': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
# room2 = {'pin': 15, 'status': 0, 'history': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
loopDuration = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(room1['pin'], GPIO.IN)
# GPIO.setup(room2['pin'], GPIO.IN)

while(True):
    room1['history'].pop(0)
    room1['history'].append(GPIO.input(room1['pin']))

    if all(x == 0 for x in room1['history']):
        new_status = 0

    if all(x == 1 for x in room1['history']):
        new_status = 1

    if room1['status'] != new_status:
        print 'status changed'
        room1['status'] = new_status

    print room1['history']
    time.sleep(loopDuration)

GPIO.cleanup()
