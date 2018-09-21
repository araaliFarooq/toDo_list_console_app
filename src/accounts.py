accounts = []

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def add_account(self):
        if any(user["username"] == self.username for user in accounts):
            return False
        if (accounts.append(self)):
                return True
        return False   
    
    def login(self):
        _username = self.username
        _password = self.password

        if any(user["username"] == _username for user in accounts):
            if any(passwrd["password"] == _password for passwrd in accounts):
                return True
            return False
        return False    
                