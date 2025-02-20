import argparse
from main import add, deleteId, listall, list_progress, list_done, list_in_progress, update_status

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # Delete Task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    # List All Tasks
    subparsers.add_parser("list", help="List all tasks")

    # List In Progress Tasks
    subparsers.add_parser("in_progress", help="List all tasks in progress")

    # List Done Tasks
    subparsers.add_parser("done", help="List all completed tasks")

    # List Tasks That Are Not Done (Progress)
    subparsers.add_parser("progress", help="List all tasks that are not done")

    # Update Task Status
    update_parser = subparsers.add_parser("update", help="Update a task status")
    update_parser.add_argument("id", type=int, help="Task ID to update")
    update_parser.add_argument("status", type=str, help="New status")

    args = parser.parse_args()

    if args.command == "add":
        add(args.description)

    elif args.command == "delete":
        deleteId(args.id)

    elif args.command == "list":
        listall()

    elif args.command == "in_progress":
        list_in_progress()

    elif args.command == "done":
        list_done()

    elif args.command == "progress":
        list_progress()

    elif args.command == "update":
        update_status(args.id, args.status)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
