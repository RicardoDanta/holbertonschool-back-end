#!/usr/bin/python3
"""Write a Python script that, using this REST API
for a given employee ID
returns information about his/her TODO list progress"""

import requests
import json
from sys import argv


if __name__ == '__main__':
    url = requests.get("https://jsonplaceholder.typicode.com/users/" +
                       argv[1])
    todos = json.loads(url.text)
    name = todos.get("name")
    url = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                       "?userId=" + argv[1])

    todos_list = json.loads(url.text)
    tasks = len(todos_list)
    done = [task for task in todos_list if task.get("completed")]
    completed_tasks = len(done)
    print("Employee {} is done with tasks({}/{}):".
          format(name, completed_tasks, tasks))

    for task in done:
        print("\t", task.get('title'))
