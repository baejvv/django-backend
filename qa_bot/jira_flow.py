from jira import JIRA

'''
이곳에서 Jira-Python 메서드를 요청하고 가공
'''

JIRA_API_TOKEN = 'ATATT3xFfGF0BPCSXLvvdtj8ASXYwZmKFoxqck3Bv4sALQnCMUcZdjPFq_JIYuZvyWi28jDX4oVTUe8cmtLjg2QG1-X8ViR_WJdgv6LKWwcBPJVDscCMap0fzB61SVyZOsyv0ZQ53YXeoPfA38ZZ_zwUFpYr-OC5JkNKIY7pW1etn7zIig53gsQ=78742648'
auth_JIRA = ('jwbae@i-nara.co.kr', JIRA_API_TOKEN)
jira = JIRA('https://kidsworld.atlassian.net/', basic_auth=auth_JIRA)


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
def create_jira_issue(project_key, summary, descriptiom, issue_type):
    issue_dict = {
        'project': {'key': f'{project_key}'},
        'summary': f'{summary}',
        'description': f'{descriptiom}',
        'issuetype': {'name': f'{issue_type}'},
    }
    jira.create_issue(fields=issue_dict)
