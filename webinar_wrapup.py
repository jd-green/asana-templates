import requests
import json
import config

# This function creates a new project in the ATM Contributing Experts team
# using the Tech Brief template


def create_tech_brief(client, number, total):
    data1 = """
    {"data": {
            "name": "[tmp] ($num/$tot) Tech Brief",
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
    data2 = data1.replace('$num', number)
    theData = data2.replace('$tot', total)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/projects/1144443867442929/duplicate",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace('tmp', client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
        proj = json.loads(response.content)
        return(proj["data"]["new_project"]["gid"])
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
