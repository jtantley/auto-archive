import openai
import os
from log_config import handle_openai_error, handle_generic_error, clericus_logger

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def generate_openai_response(prompt, session_id):
    try:
        model_engine = 'gpt-3.5-turbo-16k'
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=150,
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
