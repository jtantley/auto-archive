# Auto-Archive: Configuration & Logging Module
# Version: v0.0.3-dev
# Path: `\core\config.py``
# Updated: 09-23-2023

import os

# API Keys from os environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')
SERP_API_KEY = os.getenv('SERP_API_KEY')

# Add more config items as needed
