#[expression for items in iterable if condition]

#Create a list of squares
# squares = [x**2 for x in range(10)]
# print(squares)

#Filter even numbers
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

#Lambda Functions - single expression functions
# add = lambda x, y: x + y
# print(add(3,5))

#map() - applies a function to each item in an iterable
# numbers = [1,2,3,4]
# squares = map(lambda x: x**2, numbers)
# print(list(squares))

#filter() - filters item based on a condiion
# evenList = filter(lambda x: x % 2 == 0, numbers)
# print(list(evenList))


#reduce() - reduces iterable list to a single number
# from functools import reduce
# product = reduce(lambda x, y: x * y, numbers)
# print(product)


#os modules - provides functions to iteract with the operating system
# import os

# print(os.getcwd())
# os.mkdir("test_dire")
# os.remove("file.txt")

#sys Module - provides access to system-specific parameters and functions
# import sys

# print(sys.argv)
# print(sys.version)


#Project 1 : Command-Line Task Manager
import os
from datetime import date

#File to store tasks
FILE_NAME = "tasks.txt"

#Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status, priority, deadline = line.strip().split("|")
                tasks[int(task_id)] = {"title": title, "status": status, "priority": priority, "deadline": deadline}
    return tasks

#Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}  | {task['priority']} | {task['deadline']}\n")

#Add a new task
def add_task(tasks):
    title = input("Enter task title:")
    task_id = max(tasks.keys(), default = 0) + 1
    tasks[task_id] = {"title": title, "status": "Incomplete", "priority": "Normal", "deadline": "None"}
    print(f"Task '{title}' added.")
    
#View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']} - {task['priority']} - {task['deadline']}")

#Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else: 
        print("Task ID not found.")
        
#Set Priority
def set_priority(tasks):
    task_id = int(input("Enter the task ID to set priority for: "))
    if task_id in tasks:
        priority_id = int(input("Enter which priority you want to set: (1. Normal 2. Urgent 3. Very Urgent): "))
        if priority_id == 1:
            tasks[task_id]['priority'] = "Normal"
        elif priority_id == 2:
            tasks[task_id]['priority'] = "Urgent"
        elif priority_id == 3:
            tasks[task_id]['priority'] = "Very Urgent"
        else:
            print("No Wrong Option Selected. Choose Again.")
            set_priority(tasks)
    else: 
        print("Task ID not found.")
        
#Set Deadline
def set_deadline(tasks):
    task_id = int(input("Enter the task ID to set deadline for: "))
    if task_id in tasks:
        print(f"{tasks[task_id]} is selected.")
        deadline = int(input("Enter deadline in days from current date: "))
        try:
            if deadline > 0:
                tasks[task_id]['deadline'] = str(deadline) + " days from " + str(date.today())
        except ValueError:
            print("Input is not numeric. Enter again")
            set_deadline(tasks)
    else: 
        print("Task ID not found.")

#Delete a Task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else: 
        print("Task ID not found.")

#Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1.Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Set Priority")
        print("5. Set Deadline")
        print("6. Delete Task")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            set_priority(tasks)
        elif choice == "5":
            set_deadline(tasks)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("Goodbye!!!")
            break
        else:
            print("Invalid Choice. Please Try Again.")
            
if __name__ == "__main__":
    main()