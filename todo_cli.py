# Import necessary modules
import json  # To read and write JSON files
import os    # To check if the file exists

# Name of the file where tasks will be stored
TASK_FILE = "tasks.json"

# Function to load tasks from the JSON file
def load_tasks():
    # Check if the file exists; if not, return an empty list
    if not os.path.exists(TASK_FILE):
        return []
    
    # Open the file and load tasks using json
    with open(TASK_FILE, "r") as file:
        return json.load(file)

# Function to save tasks to the JSON file
def save_tasks(tasks):
    # Write the tasks to the file in a nicely formatted way
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(tasks, task_name):
    tasks.append({"task": task_name, "completed": False})  # Add task to the list
    print("✅ Task added.")

# Function to display all tasks
def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")  # If the task list is empty
        return
    
    # Loop through tasks and display each with its status
    for i, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        print(f"{i + 1}. {task['task']} [{status}]")

# Function to delete a task by its index
def delete_task(tasks, index):
    try:
        removed = tasks.pop(index)  # Remove task at the given index
        print(f"🗑️ Deleted: {removed['task']}")
    except IndexError:
        print("⚠️ Invalid task number.")  # If index is out of range

# Function to mark a task as completed
def mark_done(tasks, index):
    try:
        tasks[index]["completed"] = True  # Set the task status to completed
        print("🎉 Task marked as completed.")
    except IndexError:
        print("⚠️ Invalid task number.")  # If index is out of range

# Main program function
def main():
    tasks = load_tasks()  # Load tasks from the file

    # WHILE LOOP: Keeps running until the user chooses to exit
    while True:
        # Display menu options
        print("\n📝 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. Exit")

        # Ask the user to make a choice
        choice = input("Enter your choice (1-5): ")

        # IF-ELIF-ELSE ladder to handle different menu choices
        if choice == "1":
            # User chooses to add a task
            name = input("Enter task: ")
            add_task(tasks, name)

        elif choice == "2":
            # User chooses to view all tasks
            list_tasks(tasks)

        elif choice == "3":
            # User wants to mark a task as done
            list_tasks(tasks)  # Show current tasks
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(tasks, index)
            except ValueError:
                print("⚠️ Invalid input.")  # Handles non-integer input

        elif choice == "4":
            # User wants to delete a task
            list_tasks(tasks)  # Show current tasks
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, index)
            except ValueError:
                print("⚠️ Invalid input.")  # Handles non-integer input

        elif choice == "5":
            # User wants to exit the program
            save_tasks(tasks)  # Save all tasks before exiting
            print("💾 Tasks saved. Goodbye!")
            break  # Exit the while loop

        else:
            # Handles any invalid menu choice
            print("⚠️ Invalid choice. Try again.")

# Entry point: Only run the program if this script is executed directly
if __name__ == "__main__":
    main()
