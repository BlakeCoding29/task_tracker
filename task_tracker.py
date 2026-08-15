print("Task Tracker")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

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
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nToday's Tasks")

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']}")

            try:
                task_number = int(input("Enter the task number you want to delete: "))

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Deleted: {deleted_task['task']}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")            

    elif choice == "5":
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