# Auto-Archive: Clericus Module
# Version: v0.0.3-dev
# Path: `\core\clericus.py`
# Updated: 09-21-2023

# 09-20-2023: Added function call handling; error handling; functional conversational context memory
# 09-21-2023: Added logging; added function call response handling; added session ID parameter to conversation history; added web search function; split clericus.py code into smaller modules that are in the `core/clericus_modules` directory.

#############################
# ⚠️ ACTIVE DEVELOPMENT ⚠️ #
## ## ## ## ## ## ## ## ## ##

from dotenv import load_dotenv
from log_config import clericus_logger
from clericus_modules.web_search import perform_web_search
from clericus_modules.openai_module import generate_openai_response
from clericus_modules.error_handling import handle_openai_error, handle_generic_error

load_dotenv()

def generate_response(user_input, session_id):
    try:
        assistant_reply = generate_openai_response(user_input, session_id)
        if 'web_search' in assistant_reply:
            search_results = perform_web_search(user_input)
            return search_results
        return assistant_reply
    except Exception as e:
        return handle_generic_error(e, clericus_logger)
