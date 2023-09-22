# Clericus Module: Error Handling
# Updated: 09-21-2023
# Path: `\core\clericus_modules\error_handling.py`
# Version: v0.0.3-dev

import os
import logging
from log_config import clericus_logger


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
