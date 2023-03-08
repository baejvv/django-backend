def send_loading_message(user_name):
    text = f'{user_name}님이 티켓을 등록중입니다 :loading:'
    return text


def send_loading_options():
    text = '티켓이 등록된 Jira 프로젝트의 에픽, 컴포넌트 등을 가져오고 있습니다. :loading:'
    return text


def get_trigger_button():
    text = [
        {
               "type": "section",
               "text": {
                   "type": "plain_text",
                   "text": "안녕하세요. Jira 티켓을 등록하시겠어요?",
                   "emoji": True
               }
           },
           {
               "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "네!",
                            "emoji": True
                        },
                        "value": "userSelectTriggerBtn",
                        "action_id": "action_user_select_trigger_btn"
                    }
                ]
           }
    ]
    return text


def open_reaction_modal():
    text = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "종원의 심복",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "티켓 등록",
            "emoji": True
        },
        "close": {
            "type": "plain_text",
            "text": "등록 취소",
            "emoji": True
        },
        "blocks": [
            {
                "type": "input",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "작업, 버그 등..",
                        "emoji": True
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "작업",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "버그",
                                "emoji": True
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "스토리(미구현)",
                                "emoji": True
                            },
                            "value": "value-2"
                        }
                    ],
                    "action_id": "userSelectType-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "티켓의 유형을 선택해주세요.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "직접입력",
                        "emoji": True
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "조금만 기다려주세요.",
                                "emoji": True
                            },
                            "value": "value-0"
                        }
                    ],
                    "action_id": "userSelectProject-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "프로젝트 리스트 로딩 중.. :loading:",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "userInputSummary-action"
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
                    "action_id": "userInputDescription-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "내용 (Jira Ticket Description)",
                    "emoji": True
                }
            }
        ]
    }
    return text


def open_keyword_modal():
    text = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "My App",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "티켓 등록",
            "emoji": True
        },
        "close": {
            "type": "plain_text",
            "text": "등록 취소",
            "emoji": True
        },
        "blocks": [
            {
                "type": "input",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "직접입력",
                        "emoji": True
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "직접입력",
                                "emoji": True
                            },
                            "value": "value-0"
                        }
                    ],
                    "action_id": "userSelectProject-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "프로젝트 리스트 로딩 중.. :loading:",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "userInputSummary-action"
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
                    "action_id": "userInputDescription-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "내용 (Jira Ticket Description)",
                    "emoji": True
                }
            }
        ]
    }
    return text