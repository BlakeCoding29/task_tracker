print("Task Tracker")

tasks = []

task = input("Enter a task, or type done: ")

while task.lower() != "done":
    tasks.append(task)
    task = input("Enter another task, or type done: ")

completed = input("Did you complete them today? yes/no: ").lower()

print("\nToday's Tasks")

for task in tasks:
    completed = input(f"Did you complete '{task['task']}'? yes/no: ").lower()

    if completed in ["yes", "y"]:
        task["completed"] = True

print("\nToday's Tasks")

for task in tasks:
    if task["completed"]:
        status = "Completed"
    else:
        status = "Not Completed"

    print(f"- {task['task']} - {status}")

print(f"\nTotal tasks: {len(tasks)}")