# main.py

import tkinter as tk
from tkinter import messagebox
from task_manager import TaskManager
from task import Task

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List (OOP)")

        self.task_manager = TaskManager()

        self.build_ui()
        self.update_listbox()

    def build_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5)
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        self.listbox = tk.Listbox(self.frame, width=50, selectmode=tk.SINGLE)
        self.listbox.grid(row=1, column=0, columnspan=2, pady=10)

        self.complete_button = tk.Button(self.frame, text="Mark Complete", command=self.complete_task)
        self.complete_button.grid(row=2, column=0)
        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1)

    def add_task(self):
        desc = self.task_entry.get().strip()
        if desc:
            self.task_manager.add_task(Task(desc))
            self.task_entry.delete(0, tk.END)
            self.update_listbox()

    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.task_manager.complete_task(index)
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Select a task to mark as complete.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.task_manager.delete_task(index)
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            self.listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
