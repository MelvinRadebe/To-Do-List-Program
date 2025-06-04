
import os
from task import Task

class TaskManager:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def load_tasks(self):
        self.tasks.clear()
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = [Task.from_file_format(line) for line in f]

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(task.to_file_format() + "\n")
