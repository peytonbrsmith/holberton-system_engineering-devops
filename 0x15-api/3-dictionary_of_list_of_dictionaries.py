#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    etasks = {}
    for user in users:
        eid = user.get("id")
        etasks['{}'.format(eid)] = []
        for task in tasks:
            userId = task.get('userId')
            if userId == int(eid):
                info = {}
                info["username"] = user.get('username')
                info["completed"] = task.get('completed')
                info["task"] = task.get('title')
                etasks[str(eid)].append(info)

    with open('todo_all_employees.json'.format(eid), 'w') as f:
        jsn = json.dumps(etasks, sort_keys=True)
        f.write(jsn)
