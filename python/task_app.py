import tkinter as tk
from tkinter import messagebox
import os

# Directory to store tasks
TASK_DIR = 'tasks'

# Ensure the directory exists
if not os.path.exists(TASK_DIR):
    os.makedirs(TASK_DIR)

# Function to list task files in the directory
def list_task_files():
    return [f for f in os.listdir(TASK_DIR) if os.path.isfile(os.path.join(TASK_DIR, f))]

# Function to load tasks (filenames as tasks)
def load_tasks():
    return list_task_files()

# Function to save a task to an individual file
def save_task(title, body):
    task_file = os.path.join(TASK_DIR, f"{title}.txt")
    with open(task_file, 'w') as f:
        f.write(body)

# Function to load a task's content
def load_task_content(task_title):
    task_file = os.path.join(TASK_DIR, f"{task_title}.txt")
    with open(task_file, 'r') as f:
        return f.read()

# Function to delete a task file
def delete_task_file(task_title):
    task_file = os.path.join(TASK_DIR, f"{task_title}.txt")
    if os.path.exists(task_file):
        os.remove(task_file)

# Function to update the task list display
def update_task_listbox():
    task_listbox.delete(0, tk.END)  # Clear current list
    tasks = load_tasks()
    for task in tasks:
        task_listbox.insert(tk.END, task.replace(".txt", ""))

# Function to add a task
def add_task():
    task_title = task_entry.get()
    task_body = task_body_text.get("1.0", tk.END).strip()
    
    if task_title and task_body:
        save_task(task_title, task_body)
        update_task_listbox()
        task_entry.delete(0, tk.END)
        task_body_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Both title and body are required.")

# Function to view a selected task
def view_task():
    try:
        selected_task_idx = task_listbox.curselection()[0]
        task_title = task_listbox.get(selected_task_idx)
        task_body = load_task_content(task_title)
        
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task_title)
        task_body_text.delete("1.0", tk.END)
        task_body_text.insert(tk.END, task_body)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to view.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_idx = task_listbox.curselection()[0]
        task_title = task_listbox.get(selected_task_idx)
        delete_task_file(task_title)
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("My Note")

# Task title input field
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=1, column=0, padx=10, pady=10)
# Create a frame to hold the buttons side by side
button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

# Add task button inside the frame
add_button = tk.Button(button_frame, text="Add ", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

# View task button inside the frame
view_button = tk.Button(button_frame, text="View ", command=view_task)
view_button.pack(side=tk.LEFT, padx=5)

# Delete task button inside the frame
delete_button = tk.Button(button_frame, text="Delete ", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Task body text area
task_body_text = tk.Text(root, height=10, width=50) 
task_body_text.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

# Task listbox
task_listbox = tk.Listbox(root, width=20, height=10)
# Position next to the text box
task_listbox.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)


# Update the task listbox with the task files
update_task_listbox()

# Start the Tkinter event loop
root.mainloop()
