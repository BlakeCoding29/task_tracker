print("Task Tracker")

task = input("What task do you want to track? ")
completed = input("Did you complete it today? yes/no ").lower()

print("\nToday's Task")
print("Task:", task)

if completed == "yes" or completed == "y":
    print("Task completed")
else:
    print("Task not completed")
