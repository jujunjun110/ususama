# coding: utf-8
import requests
import yaml
import logging
from datetime import datetime

token_path = './token-file.yml'
token_file = open(token_path)
token = yaml.load(token_file)['token']
logger = logging.getLogger('logger.main')


class Slack:

    def post_status(self, room1, room2):
        emoji = self.decide_status(room1, room2)
        message = 'Last Update: %s' % datetime.now().strftime('%H:%M')

        profile = '{"status_emoji": "%s", "status_text": "%s"}' % (emoji, message)
        response = requests.post('https://slack.com/api/users.profile.set', params={
            'token': token,
            'profile': profile
        })

        logger.debug(response.json())

    def decide_status(self, room1, room2):
        if room1 and room2:
            return ":o:"
        if room1 or room2:
            return ":warning:"
        if not room1 and not room2:
            return ":x:"
