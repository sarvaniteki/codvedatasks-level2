import json
import os
FILE_NAME = "task.js"
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
def save_task():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks,file,indent=4)
def add_task():
    task_name = input("Enter the task name=").strip()
    if task_name == "":
        print("task cannot be empty")
        return
    tasks = load_tasks()
    tasks.append({"task":task_name,"completed": False})
    save_task(tasks)
    print("Task added successfully!")
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("no tasks found.")
        return
    for index, task in enumerate(tasks,start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}.{task['task']}{status}")
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete:"))
        tasks.pop(task_no - 1)
        save_task(tasks)
        print("task deleted successfully!")
    except(IndexError, ValueError):
        print("Invalid task number!")
def mark_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_no = int(input("enter task number to mark as done: "))
        tasks[task_no - 1] ["completed"] = True
        save_task(tasks)
        print("task marked as completed!")
    except (IndexError,ValueError):
        print("Invalid task number!")
def todo_menu():
    while True:
     print("1.add task")
     print("2.delete task")
     print("3.view task")
     print("4.mark as task")
     print("5.exit")
     choice = input("enter the values 1-5:")
     if choice == "1":
        add_task()
     elif choice == "2":
        delete_task()
     elif choice == "3":
        view_task()
     elif choice == "4":
        mark_task()
     elif choice == "5":
        print("exit")
        break
     else:
        print("plzz select a number...")
if __name__ == "__main__":
     todo_menu()







