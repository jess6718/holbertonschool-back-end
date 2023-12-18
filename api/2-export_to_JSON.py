#!/usr/bin/python3
"""Records all tasks that are owned by this employee"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # return user
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    # return todo filter by userID
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    # dynamic file name
    filename = "{}.json".format(user["id"])

    user_todos = [{"task": todo["title"], "completed": todo["completed"],
                   "username": user["username"]} for todo in todos]
    export = {sys.argv[1]: user_todos}
    # close file when written is completed
    with open(filename, "w") as output:
        json.dump(export, output)
