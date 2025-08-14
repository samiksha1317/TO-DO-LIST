import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

def refresh_listbox():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks, start=1):
        listbox.insert(tk.END, f"{idx}. {task}")

def add_task():
    task_text = entry.get().strip()
    if task_text:
        tasks.append(task_text)
        entry.delete(0, tk.END)
        refresh_listbox()
    else:
        messagebox.showwarning("Oops", "Task cannot be empty.")

def delete_task():
    try:
        sel_index = listbox.curselection()[0]
        tasks.pop(sel_index)
        refresh_listbox()
    except IndexError:
        messagebox.showwarning("Oops", "Select a task first.")

def mark_done():
    try:
        sel_index = listbox.curselection()[0]
        tasks[sel_index] = f"{tasks[sel_index]} ✅"
        refresh_listbox()
    except IndexError:
        messagebox.showwarning("Oops", "Select a task first.")

def edit_task():
    try:
        sel_index = listbox.curselection()[0]
        current_text = tasks[sel_index]
        new_text = simpledialog.askstring("Edit Task", "Change the task:", initialvalue=current_text)
        if new_text and new_text.strip():
            tasks[sel_index] = new_text.strip()
            refresh_listbox()
    except IndexError:
        messagebox.showwarning("Oops", "Select a task first.")

root = tk.Tk()
root.title("My To-Do List")
root.geometry("350x450")
root.config(bg="#f5f5f5")

tk.Label(root, text="📝 My To-Do List", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=25, bd=2, relief="solid")
entry.pack(pady=8)

btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add", command=add_task, bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Edit", command=edit_task, bg="#2196F3", fg="white", width=10).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Done", command=mark_done, bg="#FFC107", fg="black", width=10).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", command=delete_task, bg="#F44336", fg="white", width=10).grid(row=1, column=1, padx=5, pady=5)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=15, bd=2, relief="solid", selectbackground="#d1e7dd")
listbox.pack(pady=10)

root.mainloop()
