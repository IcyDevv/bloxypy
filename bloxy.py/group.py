"""
MIT License

Copyright (c) 2021 IcyDevv

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
from .utils.classes import *
import json


class Group:

    def __init__(self, name, id, description, owner):
        self.name = name
        self.id = id
        self.description = description
        self.owner = owner


    async def get_group_roles(self):
        data = requests.get(url=f'https://groups.roblox.com/v1/groups/{self.id}/roles').json()
        roles = []
        for i in data['roles']:
            roles.append(Role(i['name'], i['id'], i['rank'], i['memberCount']))
        return roles
    
    
    async def user_is_in_group(self, userid):
        data = requests.get(url=f'https://groups.roblox.com/v1/groups/{self.id}/members').json()
        user = []
        for i in data['members']:
            if i == userid:
                user = [userid]
                return True
            else:
                return False
        return user   
    
                

