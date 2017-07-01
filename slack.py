# coding: utf-8
import requests

token = 'sample'

class Slack:
    def postStatus(self, room1, room2):

        emoji = self.decideStatus(room1, room2)
        profile = '{"status_emoji": "%s"}' % emoji
        print profile
        response = requests.post('https://slack.com/api/users.profile.set', params = {
            'token': token,
            'profile': profile
        })

        print response.json()

    def decideStatus(self, room1, room2):
        if room1 and room2:
            return ":o:"
        if room1 or room2:
            return ":warning:"
        if not room1 and not room2:
            return ":x:"
