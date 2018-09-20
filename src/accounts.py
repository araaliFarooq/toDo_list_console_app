accounts = []

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # method to enable us acess class attributes as items 
    def __getitem__(self,item):
        return getattr(self, item) 
    
    # method to enable us display class objects as dictionaries 
    def __repr__(self):
        return repr(self.__dict__)
    
    def add_account(self):
        if any(user["username"] == self.username for user in accounts):
            return False
        accounts.append(self)
        return True
    
    def login(self):
        _username = self.username
        _password = self.password

        if any(user["username"] == _username for user in accounts):
            if any(passwrd["password"] == _password for passwrd in accounts):
                return True
            return False
        return False    
                