import re

class Validation:

    @staticmethod
    def validate_input_type(input):
        try:
           _input = int(input)
        except ValueError:
            return "Input should be an interger"

    @staticmethod
    def validate_task(title):
        if not title:
            return "No title was given"
        if title == "  ":
            return "No title was given"

    @staticmethod
    def auth_validation(name, user_name, email, gender, password):
        if name == user_name:
            return "name and username should be different"
        if not name:
            return "name is missing"
        if name == " ":
            return "name is missing"
        if len(name) < 4:
            return "name should be more than 4 characters long"
        if not user_name:
            return "username is missing"
        if user_name == " ":
            return "username is missing"
        if len(user_name) < 4:
            return "username should be more than 4 characters long"
        if not email:
            return "email is missing"
        if email == " ":
            return "email is missing"
        if re.match("[^@]+@[^@]+\.[^@]+", email) == None:
            return "bad email format supplied"    
        if not password:
            return "password is missing"
        if password == "  ":
            return "password is missing"
        if re.match("r'^(?=.*[a-zA-Z\d\S])(?=.*[!@#$%^&*+-_])[a-zA-Z\d!@#$%^&_*_+-_]{6,10}$'", password) == None:
            return "password should contain A capital letter, a small letter, a digit and a special character"    
        if gender == "  ":
            return "gender is missing"
        if not gender:
            return "gender is missing"    

    @staticmethod
    def login_validation(username, password):
        if not username:
            return "username is missing"
        if username == " ":
            return "username is missing"
        if not password:
            return "password is missing"
        if password == " ":
            return "password is missing"
        if re.match("r'^(?=.*[a-zA-Z\d\S])(?=.*[!@#$%^&*+-_])[a-zA-Z\d!@#$%^&_*_+-_]{5,10}+$'",password) == None:
            return "password should contain A capital letter, a small letter, a digit and a special character"      

    @staticmethod
    def email_change_validation(email):
        if not email:
            return "email is missing"
        if email == " ":
            return "email is missing"
        if re.match("[^@]+@[^@]+\.[^@]+", email) == None:
            return "bad email format supplied"

    @staticmethod
    def validate_characters(input):
        if re.search('[a-zA-Z]', input) != None:
            return True
        return False

    @staticmethod
    def validate_email(email):
        if len(email) > 4:
            if re.match("[^@]+@[^@]+\.[^@]+", email) != None:
                return True
            return False
        return False    

                    