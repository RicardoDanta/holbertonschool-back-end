#!/usr/bin/python3
"""Write a Python script that, using this REST API
for a given employee ID
returns information about his/her TODO list progress
Code by Mauricio Miranda"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    """Script that returns information about user todo list"""
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".
                     format(argv[1])).json()
    user_name = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                             format(argv[1])).json()
    completed_tasks = 0
    uncompleted_tasks = 0
    for i in url:
        if i["completed"] is True:
            completed_tasks = completed_tasks + 1
    for i in url:
        if i["completed"] is False:
            uncompleted_tasks = uncompleted_tasks + 1
    print("Employee {} is done with tasks ({}/{}):".
          format(user_name["name"], completed_tasks,
                 (completed_tasks + uncompleted_tasks)))
    for i in url:
        if i["completed"] is True:
            print("\t {}".format(elem["title"]))
