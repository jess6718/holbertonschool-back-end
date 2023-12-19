#!/usr/bin/python3
"""Records all tasks from all employees"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # return user in json format
    all_users = requests.get(url + "/users").json()
    todos_all_employees = {}

    for user in all_users:
        user_id = user["id"]
        # get all todo of particular employeein json format
        todos = requests.get(url + "/todos", params={"userId": user_id}).json()
        # store todo data in dictionary format
        user_todos = [{"username": user["username"], "task": todo["title"],
                       "completed": todo["completed"]} for todo in todos]
        # store all todos of particular user and store in dictionary
        todos_all_employees[user_id] = user_todos
    # close file when written is completed
    with open("todo_all_employees.json", "w") as output:
        json.dump(todos_all_employees, output)
