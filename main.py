import json 

tasks = []
task_counter = 1

# example task: task1 = { "id": 1, "title": "study for CS", "completed": False } 

def print_tasks():
    for t in tasks:
        status = "✓" if t["completed"] else " "
        print(f"[{status}] {t['id']}: {t['title']}")

while True:
    print("\n===== WELCOME TO TASKER =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")
    choice = input("Choose an option...\n")

    if choice == "1":
        if not tasks:
            print("No tasks found!")
        print_tasks()
    elif choice == "2":
        task_title = input("Enter new task here...\n")
        task = {
                "id": task_counter,
                "title": task_title,
                "completed": False
        }
        tasks.append(task)
        task_counter += 1
    elif choice == "3":
        print_tasks()
        completed_num = input("Which task would you like to complete?\n")
        if int(completed_num) >= int(task_counter):
            print("Invalid number. Try again.")
        else: 
            completed_task = tasks[int(completed_num) - 1]
            completed_task['completed'] = True
            print_tasks()
    elif choice == "4":
        print("Bye bye!")
        break
    else:
        print("Invalid option. Please choose a number between 1-4")



