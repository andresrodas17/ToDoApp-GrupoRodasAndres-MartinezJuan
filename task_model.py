# task_model.py
class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.is_completed = False

class TaskModel:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        t = Task(self.next_id, title)
        self.tasks.append(t)
        self.next_id += 1
        return t

    def list_tasks(self):
        return self.tasks
