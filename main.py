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
    print(f"Task with id({tasks['id']}) has been added")