
# Clericus Module: OpenAI Module
# Version: v0.0.3-dev
# Path: `\core\clericus_modules\openai_module.py`
# Updated: 09-23-2023

import os
import openai
from core.logger import handle_generic_error, clericus_logger
from core.config import OPENAI_API_KEY
from typing import Union


def generate_openai_response(prompt: str, session_id: str) -> Union[str, dict]:
    """
    Generate OpenAI API response based on prompt & session ID
    """
    try:
        model_engine = os.getenv('MODEL_ENGINE', 'gpt-3.5-turbo-16k')
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=[
                {
                    "role": "system",
                    "content": "Your name is Clericus. You are a helpful assistant."
                },
                {
                    "role": "user", "content": prompt
                }
            ],
            temperature=1,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_reply = response['choices'][0]['message']['content'].strip()
        return assistant_reply
    except Exception as e:  # Catching generic exception
        return handle_generic_error(e, clericus_logger)
