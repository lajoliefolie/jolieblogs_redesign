class Userhandler():
    
    @classmethod
    def login(self, email, password):
        if email == "admin@me.com":
            return True
        else:
            return False
    
    @classmethod
    def register(self, email, password, password_confirm):
        if not (password == password_confirm):
            return "pw_nomatch"
        elif email == "admin@me.com":
            return "email_used"
        else:
            return "registered"
    
    @classmethod
    def get(self, email):
        return "admin@me.com"