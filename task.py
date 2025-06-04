# task.py

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"[✓] {self.description}" if self.completed else f"[ ] {self.description}"

    def to_file_format(self):
        return f"{'1' if self.completed else '0'}|{self.description}"

    @staticmethod
    def from_file_format(line):
        completed, description = line.strip().split("|", 1)
        return Task(description, completed == "1")
