import json
import os

# File name for saving tasks
FILE_NAME = "tasks.json"

# Load tasks from file (if exists)
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
else:
    tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

        # Save to file
        with open(FILE_NAME, "w") as f:
            json.dump(tasks, f)

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Removed: {removed}")

                # Save updated list to file
                with open(FILE_NAME, "w") as f:
                    json.dump(tasks, f)
            else:
                print("Invalid number!")

    elif choice == "4":
        print("Exiting program... Tasks saved successfully!")
        break

    else:
        print("Invalid choice. Try again.")