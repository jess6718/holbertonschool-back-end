#!/usr/bin/python3
"""Returns information about his/her TODO list with employee ID"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # return user
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    # return todo filter by userID
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    total_tasks = len(todos)
    completed_task = 0
    for todo in todos:
        if todo["completed"]:
            completed_task = completed_task + 1

    print("Employee {} is done with tasks ({}/{}):".format(
          user.get("name"), completed_task, total_tasks))

    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
