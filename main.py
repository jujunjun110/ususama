#!/usr/bin/python
# coding: utf-8

import RPi.GPIO as GPIO
import time
import logging
from slack import Slack

# room['pin'] → raspberry pi 上で利用するピン番号
# room['status'] → 現在の部屋のステータス(0: 利用不可能, 1: 利用可能)
# room['history'] → 過去7回分のセンサーの取得値を格納する配列
room1 = {'pin': 18, 'status': 0, 'history': [0] * 7}
room2 = {'pin': 27, 'status': 0, 'history': [0] * 7}

loop_duration = 1
post_success = True
slack = Slack()

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(message)s'))

fileHandler = logging.FileHandler(filename='log/log.txt')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(message)s'))

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

# GPIO（ラズパイの汎用IOピンの初期化）
GPIO.setmode(GPIO.BCM)
GPIO.setup(room1['pin'], GPIO.IN)
GPIO.setup(room2['pin'], GPIO.IN)

logger.info('LOOP START')

while(True):
    time.sleep(loop_duration)
    should_change_status = False

    for room in [room1, room2]:
        # 近接センサーの取得値は、0(近接あり) と 1（近接なし）の2値
        room['history'].append(GPIO.input(room['pin']))
        room['history'].pop(0)
        logger.debug(room['history'])

        # history の全てのステータスが、現在保存されているステータスと異なっていたらSlackステータスを更新
        if all(status != room['status'] for status in room['history']):
            should_change_status = True
            room['status'] = room['history'][0]
            logger.info([bool(room1['status']), bool(room2['status'])])

    if should_change_status or not post_success:
        for i in range(6):  # 送信は6回までリトライ
            post_success = slack.post_status(bool(room1['status']), bool(room2['status']))

            if post_success:
                break

            logger.info('Post Failure.')
            time.sleep(10)  # 待機

GPIO.cleanup()
