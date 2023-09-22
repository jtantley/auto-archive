import logging
from log_config import clericus_logger


def handle_openai_error(e, logger):
    logger.error(f'OpenAI error: {str(e)}')
    return {'error': f'OpenAI API Error: {str(e)}'}


def handle_generic_error(e, logger):
    logger.error(f'Generic error: {str(e)}')
    return {'error': f'An error occurred: {str(e)}'}
