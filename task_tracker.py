print("Task Tracker")

tasks = []

task = input("Enter a task, or type done: ")

while task.lower() != "done":
    tasks.append(task)
    task = input("Enter another task, or type done: ")

completed = input("Did you complete them today? yes/no: ").lower()

print("\nToday's Tasks")

for task in tasks:
    print("-", task)

status = "Tasks completed" if completed in ["yes", "y"] else "Tasks not completed"
print(status)