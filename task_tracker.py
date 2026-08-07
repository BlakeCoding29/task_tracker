print("Task Tracker")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Enter a task: ")

        task = {
            "task": task_name,
            "completed": False
        }

        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        print("\nToday's Tasks")

        if len(tasks) == 0:
            print("No tasks added.")
        else:
            for index, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Not Completed"

                print(f"{index}. {task['task']} - {status}")

            print(f"\nTotal tasks: {len(tasks)}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            print("\nToday's Tasks")

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']}")

            task_number = int(input("Enter the task number you completed: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked complete.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("\nToday's Tasks")

        if len(tasks) == 0:
            print("No tasks added.")
        else:
            for index, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Not Completed"

                print(f"{index}. {task['task']} - {status}")

            print(f"\nTotal tasks: {len(tasks)}")

        print("\nGoodbye!")
        break

    else:
        print("Invalid option.")