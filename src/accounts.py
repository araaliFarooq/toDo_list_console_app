accounts = []

class User:
    def __init__(self, name, username, email, age, gender, password):
        self.name = name
        self.username = username
        self.email = email
        self.age = age
        self.gender = gender
        self.password = password

    # method to enable us acess class attributes as items 
    def __getitem__(self,item):
        return getattr(self, item) 
    
    def add_account(self):
        new_user = dict(
            name = self.name,
            username = self.username,
            email = self.email,
            age = self.age,
            gender = self.gender,
            password = self.password
        )
        if any(user["username"] == self.username for user in accounts):
            return False
        accounts.append(new_user)
        return True
    
    @staticmethod
    def login(username, password):
        _username = username
        _password = password

        if any(user["username"] == _username for user in accounts):
            if any(passwrd["password"] == _password for passwrd in accounts):
                return True
            return False
        return False

    @staticmethod
    def change_password(username, old_password, new_password):
        for account in range(len(accounts)):
            if accounts[account]["username"] == username:
                if accounts[account]["password"] == old_password:
                    accounts[account]["password"] = new_password
                    return True
                return False
            return False

    @staticmethod
    def change_email(username, password, new_email):
        for account in range(len(accounts)):
            if accounts[account]["username"] == username:
                if accounts[account]["password"] == password:
                    accounts[account]["email"] = new_email
                    return True
                return False
            return False    



                