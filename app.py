import tkinter as tk
import sqlite3

# Create a database connection
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (task text)''')

# Function to add a task
def add_task(task):
    c.execute("INSERT INTO tasks VALUES (?)", (task,))
    conn.commit()

# Function to delete a task
def delete_task(task):
    c.execute("DELETE FROM tasks WHERE task=?", (task,))
    conn.commit()

# Function to get all tasks
def get_tasks():
    c.execute("SELECT * FROM tasks")
    return c.fetchall()

# Create a GUI window
window = tk.Tk()

# Add input field and buttons
task_input = tk.Entry(window)
add_button = tk.Button(window, text="Add task", command=lambda: add_task(task_input.get()))
delete_button = tk.Button(window, text="Delete task", command=lambda: delete_task(task_input.get()))
task_input.pack()
add_button.pack()
delete_button.pack()

# Add a list to display tasks
task_list = tk.Listbox(window)
task_list.pack()

# Function to update the task list
def update_task_list():
    tasks = get_tasks()
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task[0])

# Update the task list every second
window.after(1000, update_task_list)

# Run the event loop
window.mainloop()