import logging
import threading
import multiprocessing
import sys
from datetime import datetime

class dndLogger:
    def __init__(self, name = __name__, log_to_file: bool = False, file_path: str = 'dndWorldManagerLog.log', log_to_console: bool = False, level = logging.INFO):
        self.logger = logging.getLogger(name) 
        self.logger.setLevel(level)
        self.logger.propagate = False  # Avoid duplicate logs if re-instantiated

        formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s] [%(filename)s] [Thread: %(threadName)s] [PID: %(process)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Clear old handlers
        self.logger.handlers = []

        if log_to_console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        if log_to_file:
            file_handler = logging.FileHandler(file_path)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
