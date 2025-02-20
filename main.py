import json
import os
from datetime import datetime

task_file = 'tasks.json'

def add(description):
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                pass
    
    task_id = max([task['id'] for task in tasks], default = 0) + 1

    new_task = {
        'id':task_id,
        'description': description,
        'status':'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }

    tasks.append(new_task)

    with open(task_file,'w') as file:
        json.dump(tasks,file, indent=4)
    print(f"Task with id({task_id}) has been added")


def deleteId(id):
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                pass
    
    new_tasks = [task for task in tasks if task['id'] != id]
    tasks = new_tasks 

    with open(task_file, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Task ID ({id}) has been deleted")


def listall():
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except JSONDecodeError:
                pass
    
    for task in tasks:
        print(f"{task['id']} : {task['description']}")


def list_progress():
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except JSONDecodeError:
                pass
    
    for task in tasks:
        if task['status'] == 'todo':
            print(task['description'])

def list_done():
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except JSONDecodeError:
                pass
    
    for task in tasks:
        if task['status'] == 'done':
            print(task['description'])

def list_in_progress():
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                pass

    for task in tasks:
        if task['status'] == 'in_progress':  
            print(f"{task['id']} : {task['description']} (Status: {task['status']})")



def update_task(id, status):
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                pass
    
def update_status(task_id, new_status):
    tasks = []

    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                pass

    task_found = False
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = datetime.now().isoformat()
            task_found = True
            break

    if not task_found:
        print(f"Task with ID ({task_id}) not found.")
        return

    with open(task_file, 'w') as file:
        json.dump(tasks, file, indent=4)
    
    print(f"Task ID ({task_id}) has been updated to status: {new_status}")