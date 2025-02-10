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

    user_response = requests.get(f"{url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todos_response.json()

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username,
                            task["completed"], task["title"]])
