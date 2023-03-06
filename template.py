from qa_bot.jira_flow import *
import json


def send_loading_message(user_name):
    text = f'{user_name}님이 티켓을 등록중입니다 :loading:'
    return text



def send_loading_options():
    text = '티켓이 등록된 Jira 프로젝트의 에픽, 컴포넌트 등을 가져오고 있습니다. :loading:'
    return text


def select_jira_options():
    text = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Pick an item from the dropdown list"
        },
        "accessory": {
            "type": "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Select an item",
                "emoji": True
            },
            "options": [
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    },
                    "value": "value-0"
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    },
                    "value": "value-1"
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    },
                    "value": "value-2"
                }
            ],
            "action_id": "static_select-action"
        }
    }
    return text


def modal_view():
    text = {
        "title": {
            "type": "plain_text",
            "text": "{시범운영} 티켓 등록 봇",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "티켓 등록",
            "emoji": True
        },
        "type": "modal",
        "callback_id": "modal-id",
        "close": {
            "type": "plain_text",
            "text": "등록 취소",
            "emoji": True
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "현재는 시범운영 중입니다.\n필수 선택 : 프로젝트, 티켓 Summary(제목)\n 이 외 정보는 등록 후 스레드에서 선택해주세요.",
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "input",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "직접 입력",
                        "emoji": True
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-0"
                        }
                    ],
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "프로젝트를 선택해주세요.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "plain_text_input-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "티켓 제목",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "plain_text_input-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "티켓 설명(내용)",
                    "emoji": True
                }
            }
        ]
    }
    return text
