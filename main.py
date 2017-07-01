#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time
from slack import Slack
Slack = Slack()

room1 = {'pin': 18, 'status': 0, 'history': [0] * 10}
room2 = {'pin': 27, 'status': 0, 'history': [0] * 10}
loop_duration = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(room1['pin'], GPIO.IN)
GPIO.setup(room2['pin'], GPIO.IN)

while(True):
    time.sleep(loop_duration)
    need_change_status = False

    for room in [room1, room2]:
        print room['history']
        room['history'].pop(0)
        room['history'].append(GPIO.input(room['pin']))

        if all(x != room['status'] for x in room['history']):
            need_change_status = True
            room['status'] = 1 - room1['status']

    if need_change_status:
        Slack.post_status(bool(room1['status']), bool(room2['status']))

GPIO.cleanup()
