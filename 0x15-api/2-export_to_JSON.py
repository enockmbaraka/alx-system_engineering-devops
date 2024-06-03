#!/usr/bin/python3

""""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    file = f"{user_id}.json"

    user_response = requests.get("https://jsonplaceholder.typicode.com/users")

    users = user_response.json()

    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    todos = todos_response.json()

    for user in users:
        if user.get("id") == user_id:
            name = user.get("username")

    my_dict = {}
    value = []
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
