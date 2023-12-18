#!/usr/bin/python3
"""Records all tasks that are owned by this employee"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    # return user
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    # return todo filter by userID
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    # dynamic file name
    filename = "{}.csv".format(user["id"])

    # close file when written is completed
    with open(filename, mode="w", newline="") as csv_file:
        write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            write.writerow([user["id"], user["username"], todo["completed"],
                           todo["title"]])
