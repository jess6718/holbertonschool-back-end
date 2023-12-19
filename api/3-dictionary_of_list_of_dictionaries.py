#!/usr/bin/python3
"""Records all tasks from all employees"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # return user
    all_user = requests.get(url + "/users").json()

    todos_all_employees = {}

    for user in all_user:
        user_id = user["id"]
        # return all todo of particular employeein json format
        todos = requests.get(url + "/todos", params={"userid": user_id}).json()
        user_todos = [{"username": user["username"], "task": todo["title"],
                       "completed": todo["completed"]} for todo in todos]
        todos_all_employees[user_id] = user_todos
    # close file when written is completed
    with open("todo_all_employees.json", "w") as output:
        json.dump(todos_all_employees, output)
