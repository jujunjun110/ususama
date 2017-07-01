#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time

room1 = {'pin': 18, 'status': 0, 'history': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
room2 = {'pin': 15, 'status': 0, 'history': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
loopDuration = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(room1['pin'], GPIO.IN)
GPIO.setup(room2['pin'], GPIO.IN)

while(True):
    time.sleep(loopDuration)

    needChangeStatus = False
    room1['history'].pop(0)
    room1['history'].append(GPIO.input(room1['pin']))
    room2['history'].pop(0)
    room2['history'].append(GPIO.input(room1['pin']))

    if all(x == 0 for x in room1['history']) and room1['status'] = 0:
        needChangeStatus = True
        room1['status'] = 0

    if all(x == 1 for x in room1['history']) and room1['status'] = 1:
        needChangeStatus = True
        room1['status'] = 1

    if all(x == 0 for x in room2['history']) and room2['status'] = 0:
        needChangeStatus = True
        room2['status'] = 0

    if all(x == 1 for x in room2['history']) and room2['status'] = 1:
        needChangeStatus = True
        room2['status'] = 1

    if needChangeStatus:
        Slack.send(room1['status'], room2['status'])


GPIO.cleanup()
