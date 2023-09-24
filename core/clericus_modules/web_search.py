# Clericus Module: Web Search Function
# Version: v0.0.3-dev
# Path: `\core\clericus_modules\web_search.py`
# Updated: 09-23-2023

import requests
from ..logger import handle_generic_error, clericus_logger
from typing import Union
from core.config import SERPAPI_API_KEY

# Serpstack API Search Function


def perform_web_search(query: str) -> Union[dict, str]:
    try:
        search_url = f'https://api.serpstack.com/search?access_key={SERPAPI_API_KEY}&query={query}'
        response = requests.get(search_url)
        response.raise_for_status()
        search_results = response.json()
        return search_results
    except requests.exceptions.RequestException as e:
        return handle_generic_error(e, clericus_logger)
    except Exception as e:
        return handle_generic_error(e, clericus_logger)
