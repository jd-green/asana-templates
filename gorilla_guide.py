import requests
import json
import config

# This function creates a new project in the ATM Contributing Experts team
# using the Gorilla Guide Express template

def create_gg(client):
    data1 = """
    {"data": {
            "name": "[tmp] Gorilla Guide",
            "team": "1144457099343897",
            "include": ["members",
                        "task_notes",
                        "task_assignee",
                        "task_subtasks",
                        "task_attachments",
                        "task_dates",
                        "task_dependencies",
                        "task_followers",
                        "task_tags",
                        "task_projects"
                        ]
                 }
          }"""
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/projects/1125752710363254/duplicate",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=data1.replace('tmp', client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
        proj = json.loads(response.content)
        return(proj["data"]["new_project"]["gid"])
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
