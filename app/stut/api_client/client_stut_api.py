#coding: utf-8

import requests

class StutApiClient:
    def __init__(self,api_url="http://127.0.0.1:5000") -> None:
        self.access_token = None
        self.api_url = api_url
        self.current_user = None

    def auth_login(self, username, password):
        r = requests.post(f'{self.api_url}/login', 
            json={"username":f"{username}", "password":f"{password}"})
        if r.status_code == 200:
            self.access_token = r.json()['access_token']
            return True
        else:
            return False
        
    def auth_current_user(self):
        if self.access_token != None:
            r = requests.get(f'{self.api_url}/login/status', headers={"Authorization": f"Bearer {self.access_token}"})
            if r.status_code == 200:
                self.current_user = r.json()['logged_in_as']
                return True
            else:
                return False
            
    def auth_register_user(self, username, phone_number, password):
        r = requests.post(f'{self.api_url}/register', 
            json= { 
                    "username":f"{username}", 
                    "phone_number":f"{phone_number}", 
                    "password":f"{password}"
                  }
        )
        if r.status_code == 201:
            return True, r.json()
        else:
            return False, r.json()
    
            
    def get_current_user(self):
        return self.current_user
    
    def get_access_token(self):
        return self.access_token
    

