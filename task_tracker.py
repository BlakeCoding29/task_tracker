print("Task Tracker")

task1 = input("Enter task 1: ")
task2 = input("Enter task 2: ")
task3 = input("Enter task 3: ")
completed = input("Did you complete them today? yes/no ").lower()

tasks = [task1, task2, task3]

print("\nToday's Tasks")

for task in tasks:
    print("-", task)

status = "Tasks completed" if completed in ["yes", "y"] else "Tasks not completed"
print(status)