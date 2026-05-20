# factory_logger.py

from abc import ABC, abstractmethod


# PRODUCT
class Logger(ABC):

    @abstractmethod
    def write_log(self, message):
        pass


# CONCRETE PRODUCTS
class FileLogger(Logger):

    def write_log(self, message):
        print(f"[FILE] {message}")


class DatabaseLogger(Logger):

    def write_log(self, message):
        print(f"[DATABASE] {message}")


# CREATOR
class LoggerFactory(ABC):

    @abstractmethod
    def create_logger(self):
        pass


# CONCRETE CREATORS
class FileLoggerFactory(LoggerFactory):

    def create_logger(self):
        return FileLogger()


class DatabaseLoggerFactory(LoggerFactory):

    def create_logger(self):
        return DatabaseLogger()


# TEST
factory = FileLoggerFactory()
logger = factory.create_logger()
logger.write_log("User logged in")

factory2 = DatabaseLoggerFactory()
logger2 = factory2.create_logger()
logger2.write_log("Saving activity")
