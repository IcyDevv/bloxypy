"""
MIT License

Copyright (c) 2020 darealzz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import asyncio
from .utils.errors import *
from .group import Group
import json
from .user import User
from bs4 import BeautifulSoup

class Client:

    def __init__(self, Cookie=None):
        self.Cookie = Cookie
        if self.Cookie:
            self.cookies = {'.ROBLOSECURITY': f'{self.Cookie}'}
            self.AuthenticateCookie()


    def AuthenticateCookie(self):
        request = requests.get(url='https://www.roblox.com/my/profile', cookies=self.cookies)
        try:
            request.json()
        except json.decoder.JSONDecodeError:
            raise FailedAuthentication('Invalid cookie was given.')


    async def get_self(self):
        if not self.Cookie:
            raise NotAutenticated('You must be authenticated to execute this action.')
        
        base_data = requests.get(url='https://www.roblox.com/my/profile', cookies=self.cookies).json()
        status_data = requests.get(url=f'https://users.roblox.com/v1/users/{base_data["UserId"]}/status').json()
        if status_data['status'] == '':
            status_data['status'] = None

        profile_url = requests.get(url=f'https://www.roblox.com/users/{base_data["UserId"]}/profile')
        soup = BeautifulSoup(profile_url.text, "html.parser")
        try:
            about = soup.find('div', {'class': 'profile-about-content'}).pre.span.text
        except:
            about = None

        return User(base_data['UserId'], base_data['Username'], status_data['status'], about)


    async def get_group(self, groupID):
        try:
            groupID = int(groupID)
        except ValueError:
            raise ValueError(f'groupID must be an int not a {type(groupID)}.')
        
        response = requests.get(url=f'https://groups.roblox.com/v1/groups/{groupID}')
        if response.status_code == 400:
            return None

        data = response.json()
        if data['description'] == '':
            data['description'] = None


        if not data['owner']['userId']:
            owner_obj = None
        else:
            owner_obj = await self.get_user_by_id(data['owner']['userId'])

        return Group(data['name'], data['id'], data['description'], owner_obj)


    async def get_user_by_name(self, userName): 
        data = requests.get(url=f'https://api.roblox.com/users/get-by-username?username={userName}').json()

        try:
            if data['Username']:
                pass
        except:
            return None


        id_data = requests.get(url=f'https://users.roblox.com/v1/users/{data["Id"]}').json()
        if id_data['description'] == '':
            id_data['description'] = None

        status_data = requests.get(url=f'https://users.roblox.com/v1/users/{data["Id"]}/status').json()
        if status_data['status'] == '':
            status_data['status'] = None
        
        return User(data['Username'], data['Id'], status_data['status'], id_data['description'])


    async def get_user_by_id(self, userID):
        try:
            userID = int(userID)
        except ValueError:
            raise ValueError(f'userID must be an int not a {type(userID)}.')

        response = requests.get(url=f'https://users.roblox.com/v1/users/{userID}')
        if response.status_code == 404:
            return None
        
        data = response.json()
        if data['description'] == '':
            data['description'] = None

        status_data = requests.get(url=f'https://users.roblox.com/v1/users/{data["id"]}/status').json()
        if status_data['status'] == '':
            status_data['status'] = None

        return User(data['name'], data['id'], status_data['status'], data['description'])  

