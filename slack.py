# coding: utf-8
import requests
import yaml
import logging
from datetime import datetime

settings_path = './config.yml'
settings_file = open(settings_path)
settings = yaml.load(settings_file)
token = settings['token']
place = settings['place']
logger = logging.getLogger('logger.main')


class Slack:

    def post_status(self, room1, room2):
        emoji = self.decide_status(room1, room2)
        message = 'Last Update: %s (%s)' % (datetime.now().strftime('%H:%M'), place)

        profile = '{"status_emoji": "%s", "status_text": "%s"}' % (emoji, message)

        try:
            response = requests.post('https://slack.com/api/users.profile.set', params={
                'token': token,
                'profile': profile
            })
            return True

        except requests.exceptions.Timeout:
            logger.debug('Request Timeout.')
            return False

        except requests.exceptions.RequestException as e:
            logger.debug(e)
            return False

    def decide_status(self, room1, room2):
        if room1 and room2:
            return ":o:"
        if room1 or room2:
            return ":warning:"
        if not room1 and not room2:
            return ":x:"
