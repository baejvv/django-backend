import json
import ssl
import logging as logger
import os
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from slack_sdk.web.client import WebClient
from slack_sdk.errors import SlackApiError
from template import *
from jira_flow import *

# load config
# json_path = "../conf.json"
# with open(json_path, 'r') as json_file:
#     config_dict = json.load(json_file)

# slack token
SLACK_BOT_USER_TOKEN = 'xoxb-3110187730727-3676451061091-SDIyCbgo0JZl9OuA49qCGwRL'
SLACK_VERIFICATION_TOKEN = 'jjNc7msVT69RfWycrF0pqhGh'
SLACK_SIGNING_SECRET = 'ca724aa2e9c08c89de1a8b5966dc188a'
# slack client
Client = WebClient(token=SLACK_BOT_USER_TOKEN, timeout=10)
# ssl 에러 해결
ssl._create_default_https_context = ssl._create_unverified_context


class ITestQaBot(APIView):


    def post(self, request, *args, **kwargs):

        slack_message = request.data
        # 토큰 유효성 검증
        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)


        event_message = slack_message.get('event')
        user = event_message.get('user')
        text = event_message.get('text')
        channel = event_message.get('channel')
        print("사용자:", user, "ㅣ메시지:", text)
        if '!이슈' in text:
            user_name = Client.api_call(api_method='users.info',
                            params={'token': SLACK_BOT_USER_TOKEN,
                                    'user': user}
                            )['user']['real_name']
            t = Client.api_call(api_method='chat.postMessage',
                            params={'channel': channel,
                                    'text': send_loading_message(user_name)})
            print(t)


        return Response(status=status.HTTP_200_OK)
