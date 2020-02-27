import requests
import config

# This function builds a Tech Brief tracker task


def build_tb_task(project, client, number, link, pid, tid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Tech Brief #theNum",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject",
          "taskID"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560662",
            "860330517401733": "1500",
            "860297462878516": "750",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    data4 = data3.replace('theNum', number)
    data5 = data4.replace('taskID', tid)
    theData = data5.replace('theLink', link)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

# This function builds a Gorilla Guide video tracker task


def build_gg_video_task(project, client, number, link, pid, tid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Gorilla Guide Video #theNum",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject",
          "taskID"
        ],
        "custom_fields":
            {
            "1144501884560660": "1146483354888792",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    data4 = data3.replace('theNum', number)
    data5 = data4.replace('taskID', tid)
    theData = data5.replace('theLink', link)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

# This function builds a Gorilla Guide Express tracker task


def build_gge_task(project, client, number, pid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Gorilla Guide Express Rollup #theNum",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560664",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    theData = data3.replace('theNum', number)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

# This function builds a Gorilla Guide tracker task


def build_gg_task(project, client, pid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Gorilla Guide Rollup",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560665",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    theData = data2.replace('thePID', pid)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

# This function builds a blog article tracker task


def build_article_task(project, client, number, link, pid, tid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Blog Article #theNum",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject",
          "taskID"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560661",
            "860330517401733": "750",
            "860297462878516": "400",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    data4 = data3.replace('theNum', number)
    data5 = data4.replace('taskID', tid)
    theData = data5.replace('theLink', link)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# This function builds a Webinar Wrap-Up Paper tracker task


def build_wrapup_task(project, client, number, link, pid, tid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Webinar Wrap-Up Paper #theNum",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject",
          "taskID"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560662",
            "860330517401733": "1500",
            "860297462878516": "750",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    data4 = data3.replace('theNum', number)
    data5 = data4.replace('taskID', tid)
    theData = data5.replace('theLink', link)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

# This function builds a Whitepaper tracker task


def build_wp_task(project, client, number, link, pid, tid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Whitepaper #theNum",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject",
          "taskID"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560663",
            "860330517401733": "3500",
            "860297462878516": "1500",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    data4 = data3.replace('theNum', number)
    data5 = data4.replace('taskID', tid)
    theData = data5.replace('theLink', link)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def build_full_gge_task(project, client, number, link, pid, tid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Gorilla Guide Express #theNum",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject",
          "taskID"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560664",
            "860330517401733": "4500",
            "860297462878516": "2000",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    data4 = data3.replace('theNum', number)
    data5 = data4.replace('taskID', tid)
    theData = data5.replace('theLink', link)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def build_full_gg_task(project, client, number, link, pid, tid):
    data1 = """
    {
      "data": {
        "name": "[tmp] Gorilla Guide",
        "resource_subtype": "milestone",
        "assignee": null,
        "completed": false,
        "followers": [
          "50542848393516",
          "597316423178909",
          "1110471739427709"
        ],
        "notes": "theLink",
        "parent": null,
        "projects": [
          "theProject",
          "taskID"
        ],
        "custom_fields":
            {
            "1144501884560660": "1144501884560665",
            "860330517401733": "10000",
            "860297462878516": "5000",
            "1145453081034849": "thePID",
            "1145458999310530": "1145465565580000"
            },
        "workspace": "21756957370747"
      }
    }"""
    data2 = data1.replace('theProject', project)
    data3 = data2.replace('thePID', pid)
    data4 = data3.replace('theNum', number)
    data5 = data4.replace('taskID', tid)
    theData = data5.replace('theLink', link)
    try:
        response = requests.post(
            url="https://app.asana.com/api/1.0/tasks/",
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            },
            data=theData.replace("tmp", client)
            )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
