#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID using an API.
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get user's TODOs
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
