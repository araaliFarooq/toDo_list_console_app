todo_list = []

class Task:
    def __init__(self, task_id,title):
        self.task_id = task_id
        self.title   = title

    def add_task(self):
        if (todo_list.append(self)):
            return True
        return False    