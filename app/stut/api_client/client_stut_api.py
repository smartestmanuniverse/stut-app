#coding: utf-8

import requests

r = requests.post('http://127.0.0.1:5000/login', 
                  json={"username":"rick", "password":"1234"})
if r.status_code == 200:
    r = requests.get('http://127.0.0.1:5000/login/status',
                     headers={"Authorization": "Bearer " + r.json()['access_token']})
    
    print(r.json())