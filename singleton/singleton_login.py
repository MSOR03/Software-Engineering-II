# singleton_login.py
"""1.Only one instance of LoginManager can exist.
    A globlal access point to that instance is provided."""

class LoginManager:

    # This variable belongs to the class itself.
    _instance = None

    #It controls the object creation and ensures that only one instance of the class is created.
    def __new__(cls):
        if cls._instance is None:
            print("Creating Login Manager...")

            #Give access to the object and allocate memory for it.
            cls._instance = super().__new__(cls)
            cls._instance.logged_user = None
        return cls._instance

    def login(self, username):
        self.logged_user = username
        print(f"{username} logged in.")

    def show_user(self):
        print(f"Current user: {self.logged_user}")


# TEST
manager1 = LoginManager()
manager1.login("Sebastian")

manager2 = LoginManager()
manager2.show_user()

print(manager1 is manager2)
