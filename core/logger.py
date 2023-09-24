# Auto-Archive: Logging Module
# Version: v0.0.3-dev
# Path: `\core\logger.py`
# Updated: 09-23-2023

# ⚠️ ACTIVE DEVELOPMENT ⚠️ #

import os
import logging
from logging.handlers import TimedRotatingFileHandler

logs_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'logs'))

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)


def handle_generic_error(e, logger):
    logger.error(f'Generic error: {str(e)}')
    return {'error': f'A generic error occurred: {str(e)}'}


def handle_openai_error(e, logger):
    logger.error(f'OpenAI error: {str(e)}')
    return {'error': f'An OpenAI API Error: {str(e)}'}


def setup_logger(name, log_file, level=logging.INFO, log_format=None):
    # Setup as many loggers as you want

    # Set the correct log file path
    log_file_path = os.path.join(logs_dir, log_file)

    if not log_format:
        log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'

    formatter = logging.Formatter(log_format)

    handler = TimedRotatingFileHandler(
        log_file_path, when="midnight", interval=1, backupCount=30)  # Changed to log_file_path
    handler.suffix = "%Y%m%d.log"
    handler.setFormatter(formatter)
    handler.setLevel(level)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Setup logger for different modules
try:
    run_logger = setup_logger('run_logger', os.path.join(logs_dir, 'run.log'))
    run_logger.info("Initialized run_logger")
except Exception as e:
    run_logger.error("Error initializing run_logger:", exc_info=True)

try:
    document_processor_logger = setup_logger(
        'document_processor_logger', os.path.join(logs_dir, 'processor.log'))
    document_processor_logger.info("Initialized document_processor_logger")
except Exception as e:
    document_processor_logger.error(
        "Error initializing document_processor_logger:", exc_info=True)

try:
    clericus_logger = setup_logger(
        'clericus_logger', os.path.join(logs_dir, 'clericus.log'))
    clericus_logger.info("Initialized clericus_logger")
except Exception as e:
    clericus_logger.error("Error initializing clericus_logger:", exc_info=True)

try:
    routes_logger = setup_logger(
        'routes_logger', os.path.join(logs_dir, 'routes.log'))
    routes_logger.info("Initialized routes_logger")
except Exception as e:
    routes_logger.error("Error initializing routes_logger:", exc_info=True)

try:
    db_logger = setup_logger('db_logger', os.path.join(logs_dir, 'db.log'))
    db_logger.info("Initialized db_logger")
except Exception as e:
    db_logger.error("Error initializing db_logger:", exc_info=True)

# Log the directory where logs are being saved
try:
    run_logger.info("Logs are being saved in: %s", logs_dir)
except Exception as e:
    run_logger.error("Error logging logs directory:", exc_info=True)


# ---- From former `\core\clericus_modules\error_handling.py` file` ----

# Define the `\logs` directory path relative to the current file location
logs_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')

# Create `\logs` directory if it doesn't exist
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)


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


# Clericus logger for logging errors and other information
clericus_logger = setup_logger(
    'clericus_logger', os.path.join(logs_dir, 'clericus.log'))


def handle_openai_error(e, logger):
    logger.error(f'OpenAI error: {str(e)}')
    return {'error': f'OpenAI API Error: {str(e)}'}


def handle_generic_error(e, logger):
    logger.error(f'Generic error: {str(e)}')
    return {'error': f'An error occurred: {str(e)}'}
