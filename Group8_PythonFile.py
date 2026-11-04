import tkinter as tk
from tkinter import messagebox

# TASK MANAGER SYSTEM
# Group 8 - ITE 260
# Language: Python with Tkinter

PURPLE = "#6C4AB6"
DARK_PURPLE = "#3D286B"
LIGHT_PURPLE = "#F2EDFF"
WHITE = "#FFFFFF"
TEXT = "#29243A"
GREEN = "#27845C"
RED = "#C4475A"
BORDER_PURPLE = "#B8A2E8"

tasks = []


def refresh_tasks():
    task_listbox.delete(0, tk.END)

    completed = 0

    for task in tasks:
        if task["completed"]:
            task_listbox.insert(
                tk.END, "☑  " + task["title"]
            )
            completed += 1
        else:
            task_listbox.insert(
                tk.END, "☐  " + task["title"]
            )

    count_label.config(
        text=f"{len(tasks)} tasks | {completed} completed"
    )


def add_task():
    title = task_entry.get().strip()

    if not title:
        messagebox.showwarning(
            "Empty Task", "Please enter a task first."
        )
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    task_entry.delete(0, tk.END)
    refresh_tasks()


def complete_task():
    selection = task_listbox.curselection()

    if not selection:
        messagebox.showwarning(
            "No Selection", "Please select a task first."
        )
        return

    index = selection[0]
    tasks[index]["completed"] = not tasks[index]["completed"]
    refresh_tasks()
    task_listbox.selection_set(index)


def delete_task():
    selection = task_listbox.curselection()

    if not selection:
        messagebox.showwarning(
            "No Selection", "Please select a task to delete."
        )
        return

    index = selection[0]
    title = tasks[index]["title"]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Are you sure you want to delete '{title}'?"
    )

    if confirm:
        tasks.pop(index)
        refresh_tasks()


def clear_all():
    if not tasks:
        messagebox.showinfo(
            "No Tasks", "There are no tasks to clear."
        )
        return

    confirm = messagebox.askyesno(
        "Clear All Tasks",
        "Are you sure you want to delete all tasks?"
    )

    if confirm:
        tasks.clear()
        refresh_tasks()


# Main window
root = tk.Tk()
root.title("Task Manager System")
root.geometry("520x570")
root.resizable(False, False)
root.configure(bg=LIGHT_PURPLE)

# Header
header = tk.Frame(root, bg=PURPLE, pady=18)
header.pack(fill="x")

title_label = tk.Label(
    header,
    text="TASK MANAGER SYSTEM",
    font=("Arial", 18, "bold"),
    bg=PURPLE,
    fg=WHITE
)
title_label.pack()

subtitle_label = tk.Label(
    header,
    text="Organize your tasks, one step at a time.",
    font=("Arial", 10),
    bg=PURPLE,
    fg=WHITE
)
subtitle_label.pack(pady=(5, 0))

# Main content
main_frame = tk.Frame(root, bg=LIGHT_PURPLE, padx=24, pady=20)
main_frame.pack(fill="both", expand=True)

entry_label = tk.Label(
    main_frame,
    text="Enter a new task",
    font=("Arial", 11, "bold"),
    bg=LIGHT_PURPLE,
    fg=TEXT
)
entry_label.pack(anchor="w", pady=(0, 7))

# Entry with a light purple border
entry_border = tk.Frame(
    main_frame,
    bg=BORDER_PURPLE,
    padx=2,
    pady=2
)
entry_border.pack(fill="x", pady=(0, 12))

task_entry = tk.Entry(
    entry_border,
    font=("Arial", 11),
    relief="flat",
    bd=0,
    bg=WHITE,
    fg=TEXT
)
task_entry.pack(fill="x", ipady=9, padx=1, pady=1)
task_entry.bind("<Return>", lambda event: add_task())

add_button = tk.Button(
    main_frame,
    text="＋  Add Task",
    command=add_task,
    font=("Arial", 10, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground=DARK_PURPLE,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    pady=8
)
add_button.pack(fill="x", pady=(0, 15))

list_heading = tk.Label(
    main_frame,
    text="YOUR TASKS",
    font=("Arial", 11, "bold"),
    bg=LIGHT_PURPLE,
    fg=TEXT
)
list_heading.pack(anchor="w", pady=(0, 7))

list_frame = tk.Frame(
    main_frame,
    bg=WHITE,
    highlightbackground="#D8D0E8",
    highlightthickness=1
)
list_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

task_listbox = tk.Listbox(
    list_frame,
    font=("Arial", 11),
    bg=WHITE,
    fg=TEXT,
    selectbackground=PURPLE,
    selectforeground=WHITE,
    relief="flat",
    bd=0,
    activestyle="none",
    yscrollcommand=scrollbar.set
)
task_listbox.pack(side="left", fill="both", expand=True, padx=8, pady=6)
scrollbar.config(command=task_listbox.yview)

# Action buttons
button_frame = tk.Frame(main_frame, bg=LIGHT_PURPLE)
button_frame.pack(fill="x", pady=(12, 8))

complete_button = tk.Button(
    button_frame,
    text="Complete / Undo",
    command=complete_task,
    font=("Arial", 9, "bold"),
    bg=GREEN,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    pady=8
)
complete_button.pack(side="left", fill="x", expand=True, padx=(0, 5))

delete_button = tk.Button(
    button_frame,
    text="Delete Selected",
    command=delete_task,
    font=("Arial", 9, "bold"),
    bg=RED,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    pady=8
)
delete_button.pack(side="left", fill="x", expand=True, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    command=clear_all,
    font=("Arial", 9, "bold"),
    bg=DARK_PURPLE,
    fg=WHITE,
    relief="flat",
    cursor="hand2",
    pady=8
)
clear_button.pack(side="left", fill="x", expand=True, padx=(5, 0))

# Task counter
count_label = tk.Label(
    main_frame,
    text="0 tasks | 0 completed",
    font=("Arial", 9),
    bg=LIGHT_PURPLE,
    fg=TEXT
)
count_label.pack(anchor="w", pady=(3, 8))

# Footer
footer = tk.Label(
    root,
    text="Group 8 | ITE 260 | Python and Tkinter",
    font=("Arial" ),
    bg=LIGHT_PURPLE,
    fg="#716783",
    pady=8
)
footer.pack(fill="x")

root.mainloop()

