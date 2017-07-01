#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time
from slack import Slack

# room['pin'] → raspberry pi 上で利用するピン番号
# room['status'] → 現在の部屋の状態(0: 利用不可能, 1: 利用可能)
# room['history'] → 過去10回分のセンサーの取得値を格納する配列
room1 = {'pin': 18, 'status': 0, 'history': [0] * 10}
room2 = {'pin': 27, 'status': 0, 'history': [0] * 10}

loop_duration = 1
Slack = Slack()

GPIO.setmode(GPIO.BCM)
GPIO.setup(room1['pin'], GPIO.IN)
GPIO.setup(room2['pin'], GPIO.IN)

while(True):
    time.sleep(loop_duration)
    should_change_status = False

    for room in [room1, room2]:
        # 近接センサーの取得値は、0(近接あり) と 1（近接なし）の2値
        room['history'].append(GPIO.input(room['pin']))
        room['history'].pop(0)
        print room['history']

        # history の全てのステータスが、現在保存されているステータスと異なっていたらSlackステータスを変更
        if all(x != room['status'] for x in room['history']):
            should_change_status = True
            room['status'] = 1 - room1['status']

    if should_change_status:
        Slack.post_status(bool(room1['status']), bool(room2['status']))

GPIO.cleanup()
