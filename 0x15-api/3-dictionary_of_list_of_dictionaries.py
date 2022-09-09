#!/usr/bin/python3
"""Python script to export fetched data from URL to JSON dictionaries list"""
import json
import requests


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/"

    all_users = requests.get(users_url).json()

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({i.get("id"): [{
            "task": tot.get("title"),
            "completed": tot.get("completed"),
            "username": i.get("username")}
            for tot in requests.get(todos_url, params={
                "userId": i.get("id")}).json()]
            for i in all_users}, outfile)
