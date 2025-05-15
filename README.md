# ✅ Codveda Internship - Level 2 Task 1: To-Do List CLI App


This is a command-line Python application that allows users to manage a to-do list. Users can add tasks, view them, mark them as completed, and delete them. All tasks are saved in a JSON file so they persist between runs.

---

## 🧠 Features

- ➕ Add tasks
- 📋 View all tasks with completion status
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 💾 Save/load tasks from `tasks.json`
- ⚠️ Error handling (invalid task numbers, input, etc.)

---
## 📋 Sample Menu Output
📝 To-Do List Menu
1. Add Task
2. View Tasks
3. Mark as Done
4. Delete Task
5. Exit

## 📄 Sample Usage
Enter your choice (1-5): 1
Enter task: Complete Codveda Task 1
✅ Task added.

Enter your choice (1-5): 2
1. Complete Codveda Task 1 [❌]

Enter your choice (1-5): 3
Enter task number to mark as done: 1
🎉 Task marked as completed.

Enter your choice (1-5): 2
1. Complete Codveda Task 1 [✅]

## 🗃️ File Structure
todo_cli.py       # Main application
tasks.json        # Stores the to-do list between sessions

## 🛠️ Requirements
Python 3.x
No external libraries required (json and os are built-in)

## 📌 Notes
You can reset your to-do list by deleting or clearing the tasks.json file.
This is a CLI-only application for demonstration purposes.

## 🔗 Author
This project is part of my internship tasks at Codveda Technology.
#CodvedaJourney #CodvedaExperience #FutureWithCodveda

## 💻 How to Run

```bash
python todo_cli.py

