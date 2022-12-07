#!/usr/bin/python3
"""Python script that for a given employee ID
returns information about his/her TODO list progress"""

import request

url = "https://jsonplaceholder.typicode.com/todos/1"
todos = request.get(url)
if todos.status_code == 200:
    todos = todos.json()
    for i in todos["todos"]:
        print(i["title"])
