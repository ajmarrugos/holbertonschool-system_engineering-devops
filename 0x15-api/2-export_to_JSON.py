#!/usr/bin/python3
"""Python script to export fetched data from URL to JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    name = requests.get(users_url + id).json().get("username")
    task = requests.get(todos_url, params={"userId": id}).json()
    total_task = requests.get(
        todos_url, params={"userId": id, "completed": "true"}).json()

    with open(id + '.json', 'w') as outfile:
        json.dump({id: [{"task": tot.get("title"), "completed": tot.get(
            "completed"), "username": name} for tot in task]}, outfile)
