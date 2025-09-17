# import tkinter as tk

# def click(event):
#     current = str(entry.get())
#     text = event.widget.cget("text")
    
#     if text == "=":
#         try:
#             result = eval(current)
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, result)
#         except Exception as e:
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, "Error")
#     elif text == "C":
#         entry.delete(0, tk.END)
#     else:
#         entry.insert(tk.END, text)

# # Create the main window
# root = tk.Tk()
# root.title("Mini Calculator")
# root.geometry("300x400")

# # Entry field
# entry = tk.Entry(root, font="Arial 20")
# entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# # Button labels
# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["C", "0", "=", "+"]
# ]

# # Creating button grid
# for row in buttons:
#     frame = tk.Frame(root)
#     frame.pack(expand=True, fill="both")
#     for btn_text in row:
#         btn = tk.Button(frame, text=btn_text, font="Arial 18")
#         btn.pack(side="left", expand=True, fill="both")
#         btn.bind("<Button-1>", click)

# # Start the application
# root.mainloop()




# import tkinter as tk

# def click(event):
#     current = entry.get()
#     text = event.widget.cget("text")

#     if text == "=":
#         try:
#             result = eval(current)
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, result)
#         except Exception:
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, "Error")
#     elif text == "C":
#         entry.delete(0, tk.END)
#     elif text == "⌫":
#         entry.delete(len(current)-1, tk.END)
#     else:
#         entry.insert(tk.END, text)

# # Set up main window
# root = tk.Tk()
# root.title("Mini Calculator")
# root.geometry("300x450")

# # Entry widget
# entry = tk.Entry(root, font="Arial 20")
# entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# # Button layout
# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["C", "0", "=", "+"],
#     ["⌫"]
# ]

# # Create button grid
# for row in buttons:
#     frame = tk.Frame(root)
#     frame.pack(expand=True, fill="both")
#     for btn_text in row:
#         btn = tk.Button(frame, text=btn_text, font="Arial 18")
#         btn.pack(side="left", expand=True, fill="both")
#         btn.bind("<Button-1>", click)

# root.mainloop()









# import tkinter as tk

# # Function to handle button clicks
# def click(event):
#     current = entry.get()
#     text = event.widget.cget("text")

#     if text == "=":
#         try:
#             result = str(eval(current))
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, result)
#         except Exception:
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, "Error")

#     elif text == "C":
#         entry.delete(0, tk.END)

#     elif text == "⌫":
#         entry.delete(len(current) - 1, tk.END)

#     else:
#         entry.insert(tk.END, text)

# # Create main window
# root = tk.Tk()
# root.title("iOS Style Calculator")
# root.geometry("350x500")
# root.resizable(False, False)
# root.configure(bg="#000000")  # black background like iOS

# # Entry field
# entry = tk.Entry(root, font=("Helvetica", 32), bd=0, bg="#000000", fg="white", justify="right")
# entry.pack(fill=tk.BOTH, ipadx=8, ipady=20, padx=10, pady=10)

# # Button layout (like iOS)
# buttons = [
#     ["C", "⌫", "%", "/"],
#     ["7", "8", "9", "*"],
#     ["4", "5", "6", "-"],
#     ["1", "2", "3", "+"],
#     ["0", ".", "="]
# ]

# # Styling colors
# btn_colors = {
#     "default": "#333333",
#     "operator": "#ff9500",
#     "function": "#a5a5a5",
#     "text": "white",
#     "text_func": "black"
# }

# # Button rendering
# for i, row in enumerate(buttons):
#     frame = tk.Frame(root, bg="#000000")
#     frame.pack(expand=True, fill="both")

#     for btn_text in row:
#         # Define button style
#         if btn_text in ["C", "⌫", "%"]:
#             bg_color = btn_colors["function"]
#             fg_color = btn_colors["text_func"]
#         elif btn_text in ["/", "*", "-", "+", "="]:
#             bg_color = btn_colors["operator"]
#             fg_color = btn_colors["text"]
#         else:
#             bg_color = btn_colors["default"]
#             fg_color = btn_colors["text"]

#         btn = tk.Button(
#             frame,
#             text=btn_text,
#             font=("Helvetica", 22),
#             bg=bg_color,
#             fg=fg_color,
#             bd=0,
#             relief="flat"
#         )

#         # Make "0" button wider (like on iOS)
#         if btn_text == "0":
#             btn.pack(side="left", expand=True, fill="both", ipadx=35)
#         else:
#             btn.pack(side="left", expand=True, fill="both")

#         btn.bind("<Button-1>", click)

# root.mainloop()                        




































































































# #todo list














# import tkinter as tk
# from tkinter import ttk, messagebox

# class TodoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Stylish To-Do List")
#         self.root.geometry("400x500")
#         self.root.config(bg="#1e1e2f")

#         self.tasks = []

#         self.style = ttk.Style()
#         self.style.theme_use("default")
#         self.style.configure("TButton", font=("Segoe UI", 10), padding=6)
#         self.style.configure("TEntry", font=("Segoe UI", 12))
#         self.style.configure("Todo.TCheckbutton", background="#2c2c3c", foreground="white", font=("Segoe UI", 10))

#         self.create_widgets()

#     def create_widgets(self):
#         # Entry field
#         self.task_var = tk.StringVar()
#         self.task_entry = ttk.Entry(self.root, textvariable=self.task_var)
#         self.task_entry.pack(pady=15, padx=20, fill='x')

#         # Add button
#         add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
#         add_button.pack(pady=5)

#         # Frame for tasks
#         self.task_frame = tk.Frame(self.root, bg="#2c2c3c")
#         self.task_frame.pack(padx=10, pady=10, fill='both', expand=True)

#         # Scrollbar
#         self.canvas = tk.Canvas(self.task_frame, bg="#2c2c3c", highlightthickness=0)
#         self.scrollbar = ttk.Scrollbar(self.task_frame, orient="vertical", command=self.canvas.yview)
#         self.scrollable_frame = tk.Frame(self.canvas, bg="#2c2c3c")

#         self.scrollable_frame.bind(
#             "<Configure>",
#             lambda e: self.canvas.configure(
#                 scrollregion=self.canvas.bbox("all")
#             )
#         )

#         self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)

#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.scrollbar.pack(side="right", fill="y")

#     def add_task(self):
#         task_text = self.task_var.get().strip()
#         if task_text == "":
#             messagebox.showwarning("Empty Task", "Please enter a task.")
#             return

#         var = tk.BooleanVar()
#         cb = ttk.Checkbutton(
#             self.scrollable_frame,
#             text=task_text,
#             variable=var,
#             style="Todo.TCheckbutton",
#             command=lambda: self.complete_task(cb, var)
#         )
#         cb.pack(anchor='w', pady=5, padx=10)

#         # Add a delete button next to the task
#         del_btn = ttk.Button(
#             self.scrollable_frame,
#             text="X",
#             command=lambda: self.remove_task(cb, del_btn)
#         )
#         del_btn.pack(anchor='e', pady=0)

#         self.tasks.append((cb, var))
#         self.task_var.set("")

#     def complete_task(self, checkbox, var):
#         font = ("Segoe UI", 10, "overstrike" if var.get() else "normal")
#         checkbox.config(font=font)

#     def remove_task(self, checkbox, del_btn):
#         checkbox.destroy()
#         del_btn.destroy()
#         self.tasks = [task for task in self.tasks if task[0] != checkbox]

# # Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TodoApp(root)
#     root.mainloop()






