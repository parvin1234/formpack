import sys
import requests
import json
from st2common.runners.base_action import Action

class PostBookApi(Action):
    def run(self, apiUrl):
        payload = { "ID": 0,"Title": "Hello",
        "Description": "Hello World","PageCount": 0,
        "Excerpt": "Test","PublishDate": "2019-09-16T12:21:50.505Z"}
        header = {'Content-Type': 'application/json','Accept': 'application/json'}
        data = json.dumps(payload)
        response = requests.post(url=apiUrl,data=data,headers=header)
        print(response.json())

