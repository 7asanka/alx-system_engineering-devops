#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"

    user_info = requests.get("{}/users/{}".format(url, employee_id))
    employee_data = user_info.json()
    employee_name = employee_data.get("name")

    todos_info = requests.get("{}/todos?userId={}".format(
        url, employee_id))
    todos = todos_info.json()

    completed_tasks = [todo.get("title") for todo in todos
                       if todo.get("completed") is True]
    tasks_len = len(todos)
    completed_len = len(completed_tasks)

    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, employee_name,
                            task["completed"], task["title"]])
