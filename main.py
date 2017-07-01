#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(room1['pin'], GPIO.IN)
GPIO.setup(room2['pin'], GPIO.IN)

room1 = {'pin': 18, 'status': 0, 'history': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
room2 = {'pin': 15, 'status': 0, 'history': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
loopDuration = 1

while(True):
    time.sleep(loopDuration)
    needChangeStatus = False

    for room in [room1, room2]:
        room['history'].pop(0)
        room['history'].append(GPIO.input(room['pin']))

        if all(x == 0 for x in room['history']) and room['status'] = 0:
            needChangeStatus = True
            room['status'] = 0

        if all(x == 1 for x in room['history']) and room['status'] = 1:
            needChangeStatus = True
            room['status'] = 1

    if needChangeStatus:
        # Slack.send(room1['status'], room2['status'])
        print room1['status'] + ' ' + room2['status']

GPIO.cleanup()
