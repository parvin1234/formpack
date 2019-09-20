import sys
import requests
import datetime
import json
from st2common.runners.base_action import Action

class PostBookApi(Action):
    def run(self, Message,ID,Title,Description,PageCount,Excerpt):
        apiUrl = "https://slack.com/api/chat.postMessage"
        payload = {"channel": "CGQB47LKV","Message": Message}
        header = {'Content-Type': 'application/json','Accept': 'application/json','Authorization': 'Bearer xoxp-569934227830-765942071573-767364655653-c3cb75b03372ac18f70c77acf85890e3'}
        data = json.dumps(payload)
        response = requests.post(url=apiUrl,data=data,headers=header)
        


