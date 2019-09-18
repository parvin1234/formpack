import sys
import requests
import datetime
import json
from st2common.runners.base_action import Action

class PostBookApi(Action):
    def run(self, ID,Title,Description,PageCount,Excerpt):
        apiUrl = "http://fakerestapi.azurewebsites.net/api/Books"
        date = datetime.datetime.now()
        payload = { "ID": ID,"Title": Title,
        "Description": Description,"PageCount": PageCount,
        "Excerpt": Excerpt,"PublishDate": date}
        header = {'Content-Type': 'application/json','Accept': 'application/json'}
        data = json.dumps(payload)
        response = requests.post(url=apiUrl,data=data,headers=header)
        print(response.json())


