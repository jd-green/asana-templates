import requests
import json
import config


def get_url(proj_gid):
    try:
        response = requests.get(
            url="https://app.asana.com/api/1.0/projects/"+proj_gid,
            headers={
                "Authorization": config.api_key,
                "Content-Type": "text/plain; charset=utf-8",
                "Cookie": "TooBusyRedirectCount=0",
            }
            )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        proj = json.loads(response.content)
        return(proj["data"]["new_project"]["gid"])
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


get_url("1144443867442929")
