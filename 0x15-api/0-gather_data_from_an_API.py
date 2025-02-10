#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"

    user_info = requests.get("{}/users/{}".format(url, employee_id))
    employee_data = user_info.json()
    employee_name = employee_data.get("name")

    todos_info = requests.get("{}/users/{}/todos".format(url, employee_id))
    todos = todos_info.json()

    completed_tasks = [todo.get("title") for todo in todos
                       if todo.get("completed") is True]
    tasks_len = len(todos)
    completed_len = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_len, tasks_len))
    for task in completed_tasks:
        print("\t {}".format(task))
