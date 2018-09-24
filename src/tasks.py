todo_list = []

class Task:
    def __init__(self, task_id, title, status):
        self.task_id = task_id
        self.title   = title
        self.status  = status

     # method to enable us acess class attributes as items 
    def __getitem__(self,item):
        return getattr(self, item)     

    def create_task(self):
        task = dict(
            task_id = self.task_id,
            title = self.title,
            status = self.status
            )

        todo_list.append(task)
        return True

    @staticmethod
    def delete_task(task_id):
        if any(tsk["task_id"] == int(task_id) for tsk in todo_list):
            for tsk in range(len(todo_list)):
                if todo_list[tsk]["task_id"] == int(task_id):
                    del todo_list[tsk]
                    return True
                return False
        return False 

    @staticmethod
    def mark_as_finished(task_id):
        if any(tsk["task_id"] == int(task_id) for tsk in todo_list):
            for tsk in range(len(todo_list)):
                if todo_list[tsk]["task_id"] == int(task_id):
                    todo_list[tsk]["status"] = "Finished"
                    return True
                return False
            # for task in todo_list:
            #     task.update((k, "Finished") for k, v in task.iteritems() if v == "to-do")
        return False

    @staticmethod
    def delete_all_tasks():
        if len(todo_list) > 0:
            del todo_list[:]
            return True
        return False

