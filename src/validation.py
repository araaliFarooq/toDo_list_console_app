import re

class Validation:

    @staticmethod
    def validate_id_type(input):
        try:
           _id = int(input)
        except ValueError:
            return "Id should be an interger"

    @staticmethod
    def validate_task(title):
        if not title:
            return "No question title was given"
        if title == "  ":
            return "No title was given"

    @staticmethod
    def auth_validation(user_name, password):
        if not user_name:
            return "username is missing"
        if not password:
            return "password is missing"
        if user_name == "  ":
            return "username is missing"
        if password == "  ":
            return "password is missing"

    @staticmethod
    def validate_characters(input):
        if re.search('[a-zA-Z]', input) != None:
            return True
        return False         