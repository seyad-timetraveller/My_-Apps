import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASK_FILE = 'tasks.json'

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Function to update the task list display
def update_task_listbox():
    task_listbox.delete(0, tk.END)  # Clear current list
    for task in tasks:
        status = "✓" if task['status'] == 'Completed' else "✗"
        task_listbox.insert(tk.END, f"{task['title']} - {status}")

# Function to add a task
def add_task():
    task_title = task_entry.get()
    if task_title:
        tasks.append({"title": task_title, "status": "Pending"})
        save_tasks(tasks)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task title cannot be empty.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_idx = task_listbox.curselection()[0]
        del tasks[selected_task_idx]
        save_tasks(tasks)
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as completed
def mark_task_completed():
    try:
        selected_task_idx = task_listbox.curselection()[0]
        tasks[selected_task_idx]['status'] = "Completed"
        save_tasks(tasks)
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Load tasks from the file
tasks = load_tasks()

# Create the main window
root = tk.Tk()
root.title("Task Note App")

# Task input field
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=10)

# Task listbox
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# Mark as completed button
complete_button = tk.Button(root, text="Mark Completed", command=mark_task_completed)
complete_button.grid(row=1, column=2, padx=10, pady=10)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=2, padx=10, pady=10)

# Update the task listbox with loaded tasks
update_task_listbox()

# Start the Tkinter event loop
root.mainloop()
