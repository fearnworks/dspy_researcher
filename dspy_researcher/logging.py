# log_setup.py

from loguru import logger
import os
from datetime import datetime
import sys 

def setup_logging(logs_dir="./logs"):
    # Create logs directory if it doesn't exist
    os.makedirs(logs_dir, exist_ok=True)

    # Timestamp for log file naming
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Configuration for general log file
    general_log_file = f"{logs_dir}/general_{timestamp}.log"

    # Configuration for error log file
    error_log_file = f"{logs_dir}/error_{timestamp}.log"

    # Configure Loguru to log to files in addition to the default console logger
    # General log file configuration
    logger.add(general_log_file, level="DEBUG", rotation="1 week", retention="1 month", format="{time} {level} {message}")

    # Error log file configuration
    logger.add(error_log_file, level="ERROR", rotation="1 week", retention="1 month", format="{time} {level} {message}")


