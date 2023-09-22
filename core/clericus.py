# Auto-Archive: Clericus Module
# Version: v0.0.3-dev
# Path: `\core\clericus.py`
# Updated: 09-21-2023
# ⚠️ ACTIVE DEVELOPMENT ⚠️ #
## ## ## ## ## ## ## ## ## ##

import os
import logging
import openai
import requests

# Logging Setup
log_dir = '../logs'
log_file_path = os.path.join(log_dir, 'clericus.log')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

if not os.path.exists(log_file_path):
    with open(log_file_path, 'a'):
        pass

logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

openai.api_key = os.environ['OPENAI_API_KEY']
serp_api_key = os.environ['SERPAPI_API_KEY']

conversation_histories = {}

# Web search function
def perform_web_search(query):
    search_url = f"https://api.serpstack.com/search?access_key={serp_api_key}&query={query}"
    response = requests.get(search_url)
    return response.json()

def run_clericus_chatbot(messages, session_id):
    conversation_histories.setdefault(session_id, []).extend(messages)

    try:
        payload = {
            "model": "gpt-3.5-turbo-16k",
            "messages": conversation_histories[session_id],
        }

        response = openai.ChatCompletion.create(**payload)
        assistant_reply = response['choices'][0]['message']['content']

        # Web search function call
        if "web_search" in assistant_reply:
            # Using last user message as query
            search_results = perform_web_search(messages[-1]['content'])
            return search_results

        return assistant_reply

    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API Error: {e}")
        return "I encountered an error while processing your request. Please try again later."

    except Exception as generic_exception:
        logging.error(f"Unexpected Error: {generic_exception}")
        return "An unexpected error occurred. Please try again later."

def generate_response(user_input, session_id):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    return run_clericus_chatbot(messages, session_id)
