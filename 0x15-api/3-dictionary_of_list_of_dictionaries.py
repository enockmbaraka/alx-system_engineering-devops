#!/usr/bin/python3

"""Exports to-do list information of all employees to JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    file = "todo_all_employees.json"

    user_response = requests.get("https://jsonplaceholder.typicode.com/users")

    users = user_response.json()

    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    todos = todos_response.json()

    my_dict = {}
    for user in users:
        value = []
        name = user.get("username")
        user_id = user.get("id")
        for todo in todos:
            if todo.get("userId") == user_id:
                todo.update({"task": todo.get("title")})
                todo.update({"username": name})
                for _ in ["title", "id", "userId"]:
                    del todo[_]
                value.append(todo)
        my_dict[user_id] = value

    with open(file, 'w') as f:
        json.dump(my_dict, f)
