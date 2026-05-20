# factory_adapter.py

from abc import ABC, abstractmethod


# TARGET INTERFACE
class Logger(ABC):

    @abstractmethod
    def write_log(self, message):
        pass


# OLD SYSTEM
class OldLogger:

    def old_write(self, text):
        print(f"[OLD SYSTEM] {text}")


# ADAPTER
class LoggerAdapter(Logger):

    def __init__(self, old_logger):
        self.old_logger = old_logger

    def write_log(self, message):
        self.old_logger.old_write(message)


# NORMAL LOGGER
class ConsoleLogger(Logger):

    def write_log(self, message):
        print(f"[CONSOLE] {message}")


# FACTORY
class LoggerFactory:

    @staticmethod
    def create_logger(logger_type):

        if logger_type == "console":
            return ConsoleLogger()

        elif logger_type == "old":
            return LoggerAdapter(OldLogger())

        else:
            raise ValueError("Unknown logger type")


# TEST
logger1 = LoggerFactory.create_logger("console")
logger1.write_log("Normal logger")

logger2 = LoggerFactory.create_logger("old")
logger2.write_log("Adapted old logger")
