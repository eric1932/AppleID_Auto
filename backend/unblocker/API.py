import json

from requests import get

from utils import error


class API:
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def get_password(self, username):
        try:
            result = json.loads(
                get(f"{self.url}/api/?key={self.key}&action=get_password&username={username}", verify=False).text)
        except BaseException as e:
            error(e)
            return False
        else:
            if result["status"] == "success":
                return result["password"]
            else:
                return ""

    def get_config(self, task_id):
        try:
            result = json.loads(get(f"{self.url}/api/?key={self.key}&action=get_task_info&id={task_id}", verify=False).text)
        except BaseException as e:
            error(e)
            return {"status": "fail"}
        else:
            if result["status"] == "success":
                return result
            else:
                return {"status": "fail"}

    def update(self, username, password):
        try:
            result = json.loads(
                get(f"{self.url}/api/?key={self.key}&username={username}&password={password}&action=update_password",
                    verify=False).text)
        except BaseException as e:
            error(e)
            return {"status": "fail"}
        else:
            if result["status"] == "success":
                return result
            else:
                return {"status": "fail"}
