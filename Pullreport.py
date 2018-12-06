import json
from botocore.vendored import requests
import logging

DB_API_TOKEN = 'fvAA9z158sAAAAAAAAAAjrryXjKQJOc6PxuWGI7UeGdBSvezFCBNc-Yxp8EWJLJo'

def grab_data():
   global DB_API_TOKEN
   headers = {
       'Content-Type': 'application/json; charset=utf-8',
       'Authorization': 'Bearer ' + DB_API_TOKEN
   }
   payload = '{"limit": 50,"category": "groups"}'
   url = 'https://api.dropboxapi.com/2/team_log/get_events'
   r = requests.post(url, headers=headers, data=payload)

   logger = logging.getLogger()
   logger.setLevel(logging.INFO)
   logger.info(r.json().dumps)
grab_data

def lambda_handler(event, context):
   grab_data()
   return {
       'statusCode': 200,
       'body': json.dumps('Hello from Lambda!')
   }
