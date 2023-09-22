# Clericus Module: Error Handling
# Version: v0.0.3-dev
# Path: `\core\clericus_modules\error_handling.py`
# Updated: 09-21-2023

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from ..log_config import clericus_logger

# Define logs_dir variable
# Define the logs directory path relative to the current script location
logs_dir = os.path.join(os.path.dirname(__file__), 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)


def handle_openai_error(e, logger):
    logger.error(f'OpenAI error: {str(e)}')
    return {'error': f'OpenAI API Error: {str(e)}'}


def handle_generic_error(e, logger):
    logger.error(f'Generic error: {str(e)}')
    return {'error': f'An error occurred: {str(e)}'}


def setup_logger(name, log_file, level=logging.INFO, log_format=None):
    log_file_path = os.path.join(logs_dir, log_file)
    if not log_format:
        log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'
    formatter = logging.Formatter(log_format)
    handler = TimedRotatingFileHandler(
        log_file_path, when='midnight', interval=1, backupCount=30)
    handler.suffix = '%Y%m%d.log'
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


clericus_logger = setup_logger(
    'clericus_logger', os.path.join(logs_dir, 'clericus.log'))
