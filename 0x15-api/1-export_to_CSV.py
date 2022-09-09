#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
from sys import argv


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    username = requests.get(users_url + id).json().get("username")
    task = requests.get(todos_url, params={"userId": id}).json()

    with open(id + '.csv', 'w') as filecvs:
        my_writer = csv.writer(filecvs, quoting=csv.QUOTE_ALL)
        for title in task:
            my_writer.writerow([id] +
                               [username] + [title.get("completed")] +
                               [title.get("title")])
