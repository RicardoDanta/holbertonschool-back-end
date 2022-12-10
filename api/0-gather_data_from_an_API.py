#!/usr/bin/python3
"""Write a Python script that, using this REST API
for a given employee ID
returns information about his/her TODO list progress"""

import json
import requests


url = ("https://jsonplaceholder.typicode.com/todos/")
data = requests(url)
if data.status_code == 200:
    data = data.json()
    for i in data:
        print(i["title"])
