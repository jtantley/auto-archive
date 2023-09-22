# Clericus Module: Web Search Function
# Version: v0.0.3-dev
# Path: `\core\clericus_modules\web_search.py`
# Updated: 09-22-2023

import requests
import os
from ..log_config import handle_generic_error, clericus_logger

SERP_API_KEY = os.getenv('SERP_API_KEY')


def perform_web_search(query):
    try:
        search_url = f'https://api.serpstack.com/search?access_key={SERP_API_KEY}&query={query}'
        response = requests.get(search_url)
        response.raise_for_status()
        search_results = response.json()
        return search_results
    except requests.exceptions.RequestException as e:
        return handle_generic_error(e, clericus_logger)
    except Exception as e:
        return handle_generic_error(e, clericus_logger)
