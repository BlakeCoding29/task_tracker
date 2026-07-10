print("Task Tracker")

task = input("What task do you want to track? ")
completed = input("Did you complete it today? yes/no ").lower()

print("\nToday's Task")
print("Task:", task)

status = "Task completed" if completed in ["yes", "y"] else "Task not completed"
print(status)