import json
import os

from jira import JIRA
import requests

'''
이곳에서 Jira-Python 메서드를 요청하고 가공
'''

# load configs
json_path = "qa_bot/configs.json"
with open(json_path, 'r') as json_file:
    conf = json.load(json_file)

JIRA_API_TOKEN = conf['JIRA']['JIRA_API_TOKEN']
auth_JIRA = (conf['JIRA']['JIRA_ID'], JIRA_API_TOKEN)
jira = JIRA(conf['JIRA']['JIRA_URL'], basic_auth=auth_JIRA)


# 지라 프로젝트명을 담을 배열
project_name_list = []
# 지라 프로젝트 키를 담을 배열
project_key_list = []


# 전체 프로젝트를 탐색하고 name과 key list를 반환하는 함수
def get_jira_project():
    pjs = jira.projects()
    for i in pjs:
        project_name_list.append(i.name)
        project_key_list.append(i.key)
    return project_name_list, project_key_list


# 유저가 선택한 프로젝트 name으로 key를 반환하는 함수
def post_jira_project(user_select_project):
    key_index = project_name_list.index(user_select_project)
    project_key = project_key_list[key_index]
    return project_key


# view에서 넘겨받은 정보를 토대로 jira 이슈 생성
def create_jira_issue(pj, sum, desc, istp, asgn):
    issue_dict = {
        'project': {'key': f'{pj}'}, # jira project key
        'summary': f'{sum}', # str
        'description': f'{desc}', # str
        'issuetype': {'name': f'{istp}'},  # str
        'assignee': {'id': f'{asgn}'}, # jira user accountId
    }
    res = jira.create_issue(fields=issue_dict)
    print(res)


def get_jira_user_id(username):
    headers = {
        "Accept": "application/json"
    }
    response = requests.request(
        "GET",
        conf['JIRA']['JIRA_URL'] + 'rest/api/3/groupuserpicker',
        headers=headers,
        auth=auth_JIRA,
        params={
            "query": f"{username}"
        }
    )
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    return json.loads(response.text)