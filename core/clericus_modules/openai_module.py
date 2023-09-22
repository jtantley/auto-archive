# Clericus Module: OpenAI Module
# Version: v0.0.3-dev
# Path: `\core\clericus_modules\openai_module.py`
# Updated: 09-22-2023

import openai
import os
from ..log_config import handle_openai_error, handle_generic_error, clericus_logger

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY


def generate_openai_response(prompt, session_id):
    try:
        model_engine = os.getenv('MODEL_ENGINE', 'gpt-3.5-turbo-16k')
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_reply = response.choices[0].text.strip()
        return assistant_reply
    except openai.Error as e:
        return handle_openai_error(e, clericus_logger)
    except Exception as e:
        return handle_generic_error(e, clericus_logger)
