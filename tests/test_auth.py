from src.accounts import User, accounts
import unittest

class Auth_Test(unittest.TestCase):

    def setUp(self):
        self.username = "araali"
        self.username_2 = " "
        self.password = "pass"
        self.password_2 = "pass_2"
        self.accounts = [{"username":"araali", "password":"pass"}]


    def test_register(self):
        new_user = User(self.username,self.password)
        register = new_user.add_account()
        self.assertEquals(register, True)

    def test_register_user_exists_validation(self):
        new_user = User(self.username,self.password)
        register = new_user.add_account()
        self.assertEquals(register, False)

    def test_successful_login(self):
        new_user = User(self.username,self.password)
        register = new_user.add_account()
        login = new_user.login()
        self.assertEquals(login, True)

    def test_unsuccessful_login(self):
        new_user = User(self.username,self.password_2)
        register = new_user.add_account()
        login = new_user.login()
        self.assertEquals(login, False)

