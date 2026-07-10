print("Task Tracker")

task1 = input("Enter task 1: ")
task2 = input("Enter task 2: ")
task3 = input("Enter task 3: ")
completed = input("Did you complete them today? yes/no ").lower()

tasks = [task1, task2, task3]

print("\nToday's Tasks")
print("1: ", tasks[0])
print("2: ", tasks[1])
print("3: ", tasks[2])

status = "Tasks completed" if completed in ["yes", "y"] else "Tasks not completed"
print(status)