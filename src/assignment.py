'''
The expected output is a console application that
you can use to manage your to do list. 
It allows you to create an account and manipulate tasks

I have provided a structure for the code: FOLLOW INSTRUCTIONS
--------------------------------------------------------------
                    INSTRUCTIONS
--------------------------------------------------------------
1. Create a folder called src

2. Create the following files:
    - accounts.py
    - tasks.py
    - app.py

In the files, do the following:
'''
# --- accounts.py --
# This file contains code for managing your account

accounts = {}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    """
    Adds the key value pair to the accounts dictionary
    """
    pass


def login(name, password):
    """
    returns true if the password and corresponding name exist in the 
    accounts dicitionary
    """
    pass


# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = []

# Write a function creates a task


def create_task(task):
    """
    Adds the task (string value) to todo_list
    """
    pass

# Write a function deletes a task


def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    pass

# Write a function that marks a task finished


def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    pass

# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    pass


# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

# from tasks import todo_list, create_task  # import other functions as well
# from accounts import accounts, add_account  # import the function as well


if __name__ == "__main__":
    """
        Allow a person to input a name and a password

        E.g
    """
    name = input("Enter your name: ")

    """
        Let the person sign in. If there details do not exist,
        create an account for them

        E.g 
    """
    add_account("brian", "ndela35$$")


    """
        Provide options:
            1. creating a task
            2. deleting a task 
            3. deleting all tasks
            4. Marking a task finished

        E.g
    """

    print("Select Option:")
    print("1: Create Task")
# ..... skipped code
    selection = input("selection: ")

#Write code that implements the selected option

"""
The above should appear as
    Select Options:
        1. Create Task
        2 .... 
        3 ....
        4 ....

    selection:
"""

