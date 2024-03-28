import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT NOT NULL)''')

def add_task(task):
    """Add a new task to the list"""
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print("Added task:", task)

def list_tasks():
    """List all tasks"""
    c.execute("SELECT id, task FROM tasks")
    tasks = c.fetchall()
    if tasks:
        for task in tasks:
            print(f"{task[0]}: {task[1]}")
    else:
        print("No tasks found.")

def delete_task(task_id):
    """Delete a task by its ID"""
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print(f"Deleted task {task_id}")

def main():
    while True:
        print("\nSimple To-Do List App")
        print("1. Add task")
        print("2. List tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

# Close the database connection before exiting
conn.close()
