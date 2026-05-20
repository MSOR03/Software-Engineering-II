# factory_decorator_command.py

from abc import ABC, abstractmethod


# RECEIVER
class LoginSystem:

    def login(self, user):
        print(f"{user} logged in")

    def logout(self, user):
        print(f"{user} logged out")


# COMMAND INTERFACE
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# CONCRETE COMMANDS
class LoginCommand(Command):

    def __init__(self, system, user):
        self.system = system
        self.user = user

    def execute(self):
        self.system.login(self.user)


class LogoutCommand(Command):

    def __init__(self, system, user):
        self.system = system
        self.user = user

    def execute(self):
        self.system.logout(self.user)


# DECORATOR
class CommandLogger(Command):

    def __init__(self, command):
        self.command = command

    def execute(self):
        print("[LOG] Executing command...")
        self.command.execute()
        print("[LOG] Command finished")


# FACTORY
class CommandFactory:

    @staticmethod
    def create_command(command_type, system, user):

        if command_type == "login":
            command = LoginCommand(system, user)

        elif command_type == "logout":
            command = LogoutCommand(system, user)

        else:
            raise ValueError("Invalid command")

        # Add decorator automatically
        return CommandLogger(command)


# TEST
system = LoginSystem()

cmd1 = CommandFactory.create_command(
    "login",
    system,
    "Sebastian"
)

cmd1.execute()

print()

cmd2 = CommandFactory.create_command(
    "logout",
    system,
    "Sebastian"
)

cmd2.execute()
