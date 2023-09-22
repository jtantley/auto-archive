# Auto-Archive: Clericus Module
# Version: v0.0.3-dev
# Path: `\core\clericus.py`
# Updated: 09-22-2023

#############################
# ⚠️ ACTIVE DEVELOPMENT ⚠️ #
## ## ## ## ## ## ## ## ## ##

from dotenv import load_dotenv
from core.clericus_modules.web_search import perform_web_search
from core.clericus_modules.openai_module import generate_openai_response
from core.clericus_modules.error_handling import handle_generic_error
from core.clericus_modules.error_handling import clericus_logger

load_dotenv()


def generate_response(user_input, session_id):
    try:
        response = generate_openai_response(user_input, session_id)
        if 'web_search' in response:
            search_results = perform_web_search(user_input)
            return search_results
        return response
    except Exception as e:
        return handle_generic_error(e, clericus_logger)
