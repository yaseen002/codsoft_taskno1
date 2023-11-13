import tkinter as tk
from tkinter import messagebox

def add_todo():
    # Function to add a new task
    todo = entry.get()
    if todo:
        listbox.insert(tk.END, todo)
        entry.delete(0, tk.END)  # Clear the task entry
        save_to_file()

def remove_todo():
    # Function to remove a selected task
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        save_to_file()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_to_file():
    # Function to save tasks to a file
    with open("todo.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_from_file():
    # Function to load tasks from a file
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack the task list
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)

# Load existing tasks from the file
load_from_file()

# Create and pack the task entry widget
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create and pack the Add and Remove buttons
add_button = tk.Button(root, text="Add Task", command=add_todo)
add_button.pack(side=tk.LEFT, padx=5)
remove_button = tk.Button(root, text="Remove Task", command=remove_todo)
remove_button.pack(side=tk.LEFT, padx=5)

# Run the Tkinter main loop
root.mainloop()
