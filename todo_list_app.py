import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = entry.get()  # Get the text from the entry widget
    if task != "":  # Ensure the task is not empty
        listbox.insert(tk.END, task)  # Add task to the listbox
        entry.delete(0, tk.END)  # Clear the entry box
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a task from the list
def delete_task():
    try:
        selected_task_index = listbox.curselection()  # Get the selected task index
        listbox.delete(selected_task_index)  # Remove the selected task
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()  # Get the selected task index
        task = listbox.get(selected_task_index)  # Get the task text
        # Update the task with a '✔' symbol for completed tasks
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, task + " ✔")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Create the main window
window = tk.Tk()
window.title("To-Do List App")
window.configure(bg="#f5f5f5")  # Set background color

# Create a header label with a modern font and larger text
header_label = tk.Label(window, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333")
header_label.pack(pady=20)

# Create the entry widget for task input with a border
entry = tk.Entry(window, width=40, font=("Arial", 14), bd=2, relief="solid", highlightthickness=2)
entry.pack(pady=10)

# Create the add button with a custom background color and rounded corners
add_button = tk.Button(window, text="Add Task", width=20, font=("Arial", 12), bg="#4CAF50", fg="white", command=add_task, relief="raised")
add_button.pack(pady=5)

# Create the listbox to display tasks with a clean design and scroll functionality
listbox = tk.Listbox(window, width=40, height=10, font=("Arial", 14), selectmode=tk.SINGLE, bd=2, relief="solid", highlightthickness=2)
listbox.pack(pady=10)

# Create the delete button with a custom background color
delete_button = tk.Button(window, text="Delete Task", width=20, font=("Arial", 12), bg="#f44336", fg="white", command=delete_task, relief="raised")
delete_button.pack(pady=5)

# Create the mark completed button with a custom background color
completed_button = tk.Button(window, text="Mark Completed", width=20, font=("Arial", 12), bg="#FFC107", fg="black", command=mark_completed, relief="raised")
completed_button.pack(pady=5)

# Run the main event loop
window.mainloop()
