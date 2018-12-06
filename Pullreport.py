#!/usr/bin/python
import requests
import json
import csv

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
    print r.json()
grab_data()

