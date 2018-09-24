import unittest
from src.tasks import Task, todo_list

class Test_Tasks(unittest.TestCase):

    def setUp(self):
        self.title = "cleaning"
        self.task_id = len(todo_list)+1
        self.status = "to-do"
        self.status_2 = "Finished"

    def test_adding_task(self):
        task = Task(self.task_id, self.title, self.status)
        new_task = task.create_task()
        self.assertEquals(new_task, True)

    def test_deleting_task(self):
        task = Task(self.task_id, self.title, self.status)
        new_task = task.create_task()
        delete_task = Task.delete_task(self.task_id)
        self.assertEquals(delete_task, True)

    def test_deleting_all_task(self):
        task = Task(self.task_id, self.title, self.status)
        new_task = task.create_task()
        delete_all_tasks = Task.delete_all_tasks()
        self.assertEquals(delete_all_tasks, True)

    def test_finishing_task(self):
        task = Task(self.task_id, self.title, self.status)
        new_task = task.create_task()
        finish_task = Task.mark_as_finished(self.task_id)
        self.assertEquals(finish_task, True)       