import tkinter as tk
from tkinter import messagebox, filedialog

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Task list
tasks = []

# Functions
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected[0])
        tasks.remove(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_tasks():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, 'w') as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved!")

def load_tasks():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, 'r') as f:
            loaded_tasks = f.readlines()
            global tasks
            tasks = [task.strip() for task in loaded_tasks]
            update_listbox()

# Widgets
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", width=20, command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Tasks", width=20, command=load_tasks)
load_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Run the main loop
root.mainloop()

