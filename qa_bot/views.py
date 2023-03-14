import json
import ssl
from slack_sdk.web.client import WebClient
from slack_bolt import App
from slack_bolt.adapter.django import SlackRequestHandler
from jira import JIRA
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from slack_custom.views import SlackCustomView


'''
엔드포인트를 하나로 관리하기 위한 main 뷰
'''

json_path = "qa_bot/configs.json"
with open(json_path, 'r') as json_file:
    conf = json.load(json_file)


# # Jira
# JIRA_API_TOKEN = conf['JIRA']['JIRA_API_TOKEN']
# auth_JIRA = (conf['JIRA']['JIRA_ID'], JIRA_API_TOKEN)
# jira = JIRA(conf['JIRA']['JIRA_URL'], basic_auth=auth_JIRA)
# ssl 에러 해결
ssl._create_default_https_context = ssl._create_unverified_context


class QaBot(APIView):

    def post(self, request, format=None):
        slack_message = request.data

        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message, status=status.HTTP_200_OK)

        if 'event' in slack_message:
            event_message = slack_message.get('event')
            if slack_message.get('challenge') is not None:
                return Response(status=status.HTTP_200_OK, data=dict(challenge=event_message.get('challenge')))

            # ignore bot's own message
            elif event_message.get('subtype') == 'bot_message':
                return Response(status=status.HTTP_200_OK)

            elif event_message.get('reaction') == 'eyes':
                channel = event_message.get('item').get('channel')
                if channel == conf['channel']['dev']:
                    channel = conf['channel']['dev']
                    project = conf['project_key']['dev']
                    slack_view = SlackCustomView(channel, project) # Generate slack view instance
                    slack_view.post(event_message) # reaction_added event
                    return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)

