import json
import ssl
import logging as logger
import os
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from slack_sdk.web.client import WebClient
from slack_sdk.errors import SlackApiError
from template import *


# load configs
json_path = "configs.json"
with open(json_path, 'r') as json_file:
    conf = json.load(json_file)

# slack token
SLACK_BOT_USER_TOKEN = conf['SLACK']['SLACK_BOT_USER_TOKEN']
SLACK_VERIFICATION_TOKEN = conf['SLACK']['SLACK_VERIFICATION_TOKEN']
SLACK_SIGNING_SECRET = conf['SLACK']['SLACK_SIGNING_SECRET']
# slack client
Client = WebClient(token=SLACK_BOT_USER_TOKEN, timeout=10)
# ssl 에러 해결
ssl._create_default_https_context = ssl._create_unverified_context


'''

'''


@api_view(['POST', 'GET'])
def get_reactions(request):
    if request.method == 'POST':

        global event_message, user, text, channel, ts
        slack_message = request.data
        event_message = slack_message.get('event')
        if slack_message.get('challenge') is not None:
            return Response(status=status.HTTP_200_OK, data=dict(challenge=slack_message.get('challenge')))

        try:
            if event_message.get('reaction') == 'eyes':
                user = event_message.get('user')
                # text = event_message.get('text')
                type = event_message.get('item')
                channel = type.get('channel')
                ts = type.get('ts')
                t = Client.chat_postEphemeral(
                    channel=channel,
                    text='test',
                    blocks=[select_jira_options()],
                    user=user,
                    thread_ts=ts
                )
                print(slack_message)
                # run_modal()
        except AttributeError:
            # 블록킷에서 이슈 등록을 선택하여 이벤트 메시지에 payload가 담겨져 온 후 처리
            if 'payload' in slack_message.dict().keys(): # QueryDict를 파이썬dict로 반환
                payload = json.loads(slack_message.dict().get('payload')) # payload의 value를 load
                print(payload)

    return Response(status=status.HTTP_200_OK)




def run_modal():
    print("사용자:", user, "ㅣ메시지:", text)
    print(event_message)
    # 모든 지라 프로젝트 name, key 값 받아와서 저장
    project_name_list, project_key_list = get_jira_project()
    print(project_name_list)
    print(project_key_list)


    # TODO. 특정 키워드로 이슈 등록
    '''
    if '!작업' in text:
        issuetype = '작업'
        user_name = Client.api_call(api_method='users.info',
                        params={'token': SLACK_BOT_USER_TOKEN,
                                'user': user}
                        )['user']['real_name']
        t = Client.api_call(api_method='chat.postMessage',
                                params={
                                    'channel': channel,
                                    'text': send_loading_message(user_name, issuetype),
                                    'thread_ts': ts
                                })
        print(t)
        return Response(status=status.HTTP_200_OK)
    elif '!이슈' in text:
        issuetype = '버그'
        user_name = Client.api_call(api_method='users.info',
                                    params={'token': SLACK_BOT_USER_TOKEN,
                                            'user': user}
                                    )['user']['real_name']
        Client.api_call(api_method='chat.postMessage',
                        params={
                            'channel': channel,
                            'text': send_loading_message(user_name, issuetype),
                            'thread_ts': ts
                        })
        return Response(status=status.HTTP_200_OK)
        '''

    return Response(status=status.HTTP_200_OK)
