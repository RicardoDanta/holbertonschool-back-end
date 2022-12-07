#!/usr/bin/python3
"""Python script that for a given employee ID
returns information about his/her TODO list progress"""

import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/todos/1"
    todos = requests.get(url)
    if todos.status_code == 200:
        todos = todos.json()
        for i in todos:
            print(i["title"])
