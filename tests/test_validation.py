from src.validation import Validation
import unittest
import re

class Test_Validation(unittest.TestCase):
    def setUp(self):
        self.title = ""
        self.status_2 = "Finished"
        self.username = "araali"
        self.username_2 = ""
        self.password = "pass"
        self.password_2 = ""

    def test_id_validation(self):
        valid = Validation.validate_id_type("a")
        self.assertEquals(valid,"Id should be an interger")

    def test_task_validation(self): 
        valid = Validation.validate_task(self.title)
        self.assertEquals(valid,"No title was given")

    def test_passing_auth_validation(self):
        valid = Validation.auth_validation(self.username, self.password)
        self.assertEquals(valid, None)
    
    def test_failing_auth_validation(self):
        valid = Validation.auth_validation(self.username_2, self.password)
        self.assertEquals(valid, "username is missing")     

    def test_failing_auth_validation_2(self):
        valid = Validation.auth_validation(self.username, self.password_2)
        self.assertEquals(valid, "password is missing")

    def test_valid_characters(self):
        valid = Validation.validate_characters(self.username)
        self.assertEquals(valid, True)

    def test_invalid_characters(self):
        valid = Validation.validate_characters("1111111")
        self.assertEquals(valid, False)          