# Task Tracker

A beginner Python project for creating, viewing, updating, and deleting a list of daily tasks.

This project started as a simple single-task tracker and has been expanded as I learned more Python concepts.

## Features

* Add multiple tasks
* View all saved tasks
* Track each task individually
* Mark tasks as completed
* Delete tasks individually
* Display completed and incomplete task status
* Display the total number of tasks
* Menu-based navigation
* Basic input validation
* Handle invalid task number input

## Python Concepts Used

* Lists
* Dictionaries
* `while` loops
* `for` loops
* Conditional statements
* User input
* String methods
* `enumerate()`
* `len()`
* `list.append()`
* `list.pop()`
* `try` / `except`
* Updating values stored in dictionaries

## Menu Options

When the program starts, the user can choose from:

1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Exit

Each task stores both the task name and its completion status.

Example:

```python
{
    "task": "Finish homework",
    "completed": False
}
```

## How to Run

From the project directory, run:

```bash
python3 task_tracker.py
```

## Future Improvements

* Save tasks to a file
* Load previous tasks when the program starts
* Add task due dates
* Sort tasks by completion status
