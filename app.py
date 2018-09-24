from src.accounts import User, accounts
from src.tasks import todo_list, Task
from src.validation import Validation
import sys


class Menu:
    '''display'''
    def __init__(self):
        self.choices = {
            "1": self.add_user,
            "2": self.user_login,
            "3": self.quit
        }

    def display_menu(self):
        print('''
        User Menu:
        1. Add User
        2. Login
        3. Quit
        ''')

    def run(self):
        '''Display the menu and respond to 
           user input choices, 
        '''
        while True:
            self.display_menu()
            choice = raw_input("Enter an option: ").strip()
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def add_user(self):
        '''Takes user input and adds to the list'''
        username = raw_input("Enter username: ").strip()
        password = raw_input("Enter password: ").strip()

        valid = Validation.auth_validation(username, password)
        if valid:
            print(valid)
        else:    
            if not Validation.validate_characters(username):
                print("Include letters in your username")
            else:    
                new_user = User(username, password)
                if (new_user.add_account()):
                    print("User Registration successful")
                    print("")
                    self.show_users()
                else: 
                    print("User Registration failed") 
            

    def user_login(self):
        username = raw_input("enter username: ").strip()
        password = raw_input("enter password: ").strip()

        valid = Validation.auth_validation(username, password)
        if valid:
            print(valid)
        else:    
            _login = User(username, password)
            if _login.login():
                print("Sucessfully logged in")
                print("")
                while True:
                    self.show_user_menu()
                    continue
               
            else:
                print("failed to login")
    
    def show_user_menu(self):
        print('''
            User Menu:
            1. Add Task
            2. Finish Task
            3. Delete Task
            4. Delete All Tasks
            5. Quit
            ''')
        print("")
        choice = input("choose option: ").strip()
        if choice == 1:
            self.create_new_task()
        elif choice == 2:
            self.finish_a_task()
        elif choice == 3:
            self.delete_a_task()
        elif choice == 4:
            self.delete_all_tasks()
        elif choice == 5:
            self.quit()
        else:
            print("{0} is not a valid choice".format(choice))        
    
    def create_new_task(self):
        title = raw_input("Enter task title: ").strip()
        status = "to-do"
        task_id = len(todo_list)+1

        valid = Validation.validate_task(title)
        if valid:
            print(valid)
        else:
            new_task = Task(task_id, title, status)
            if(new_task.create_task()):
                print("successfully added task")
                print(" ")
                self.show_tasks()
            else:
                print("Failed to add task")    

    def show_tasks(self):
        for task in todo_list:
            print("Task Id: {0}  \nTask: {1}  \nStatus: {2} ".format(
                task["task_id"], task["title"], task["status"]
            ))

    def show_users(self):
        if len(accounts) > 0:
            for user in accounts:
                print("Username: {0}  \nPassword: {1} ".format(
                    user.username, user.password
                ))
        else:
            print("No user added yet")               

    def finish_a_task(self):
        task_id = raw_input("Enter Task Id: ").strip()

        valid = Validation.validate_id_type(task_id)
        if valid:
            print(valid)
        else:
            if (Task.mark_as_finished(task_id)):
                print("successfully finished Task")
                self.show_tasks()
            else:
                print("Task Not Updated or doest exist")


    def delete_a_task(self):
        task_id = raw_input("Enter Task Id: ").strip()

        valid = Validation.validate_id_type(task_id)
        if valid:
            print(valid)
        else:
            if (Task.delete_task(task_id)):
                print("successfully deleted Task")
            else:
                print("Task Not Deleted or doest exist")

    def delete_all_tasks(self):
        if (Task.delete_all_tasks()):
            print("successfully deleted all Tasks")
        else:
            print("No Task Deleted")        

    def quit(self):
        '''exits the system'''
        print("Thank you for using the system today")
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()