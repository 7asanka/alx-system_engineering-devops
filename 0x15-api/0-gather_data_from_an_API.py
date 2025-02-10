#!/usr/bin/python3
"""Fetches TODO list progress of an employee from a REST API"""
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todos_response.json()

    completed_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_count, total_tasks))
    for task in completed_tasks:
        print(f"\t {task}")
