# Auto-Archive: Clericus Module
# Version: v0.0.3-dev
# Path: `\core\clericus.py`
# Updated: 09-23-2023

# ⚠️ ACTIVE DEVELOPMENT ⚠️ #

import openai
import json
from typing import Union
from .clericus_modules.web_search import perform_web_search
from .clericus_modules.openai_module import generate_openai_response
from core.logger import clericus_logger, handle_generic_error
from core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_response(user_input: str, session_id: str) -> Union[str, dict]:
    """
    Generate a response based on user input and session ID.
    If 'web_search' is in the response, perform a web search.
    """
    try:
        response = generate_openai_response(user_input, session_id)
        if 'web_search' in response:
            search_results = perform_web_search(user_input)
            return json.dumps(search_results)  # Convert object to JSON string
        return response  # Assuming this is already a string
    except Exception as e:
        error_response = handle_generic_error(e, clericus_logger)
        return json.dumps(error_response)  # Convert object to JSON string
