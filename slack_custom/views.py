from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from slack_sdk.web.client import WebClient
from slack_sdk.errors import SlackApiError
from template import *
from qa_bot.jira_flow import *


json_path = "qa_bot/configs.json"
with open(json_path, 'r') as json_file:
    conf = json.load(json_file)


# Slack
SLACK_BOT_TOKEN = conf['SLACK']['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = conf['SLACK']['SLACK_APP_TOKEN']
SLACK_VERIFICATION_TOKEN = conf['SLACK']['SLACK_VERIFICATION_TOKEN']
SLACK_SIGNING_SECRET = conf['SLACK']['SLACK_SIGNING_SECRET']
Client = WebClient(token=SLACK_BOT_TOKEN, timeout=10)  # 자원 낭비를 막기 위한 Timeout


class SlackCustomView(APIView):
    # POST 응답이 올 시 모든것을 처리하는 메인 메서드이자 Slack 상호작용의 Rest Endpoint

    def __init__(self, channel, project):
        self.channel = channel
        self.project = project

    def post(self, event_message, *args, **kwargs):
        try:
            # 이모지 이벤트 감지 시 로직
            # 받은 이벤트가 이모지일 경우 key:type이므로 일부 변수 재정의
            item_user = event_message.get('item_user')
            user = event_message.get('user')
            item = event_message.get('item')
            # channel = item.get('channel')
            ts = item.get('ts')
            # reaction username return
            username, item_username = self.get_real_username(item_user, user, ts)[1:]
            print(username, item_username)
            ts_msg = self.get_message(ts)[1]
            if ts_msg is not None:
                assginee = get_jira_user_id(username)['users']['users'][0]['accountId']
                try:
                    res = create_jira_issue(self.project, ts_msg, assginee)
                    print(res)
                except Exception as e:
                    print(e, res)
                finally:
                    return Response({'list': 'test'}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_200_OK)

    # 정의된 이모지 추가 시
    def get_real_username(self, item_user, user, ts):

        username = Client.api_call(api_method='users.info',
                                    params={'token': SLACK_BOT_TOKEN,
                                            'user': user}
                                    )['user']['real_name']
        item_username = Client.api_call(api_method='users.info',
                                        params={'token': SLACK_BOT_TOKEN,
                                                'user': item_user}
                                        )['user']['real_name']
        Client.api_call(api_method='chat.postMessage',
                        params={
                            'channel': self.channel,
                            'text': send_loading_message(username),
                            'thread_ts': ts
                        })
        return Response(status=status.HTTP_200_OK), username, item_username


    # reaction이 추가된 ts로 메시지 text 가져오기
    def get_message(self, ts):
        try:
            # Call the conversations.history method using the WebClient
            # The client passes the token you included in initialization
            result = Client.conversations_history(
                channel=self.channel,
                inclusive=True,
                oldest=ts,
                limit=1
            )

            message = result['messages'][0]['text']
            return Response(status=status.HTTP_200_OK), message

        except SlackApiError as e:
            print(f"Error: {e}")
            return Response({e}, status=status.HTTP_200_OK)
