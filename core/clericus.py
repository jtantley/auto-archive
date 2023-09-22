# Auto-Archive: Clericus Module
# Version: v0.0.3-dev
# Path: `\core\clericus.py`
# Updated: 09-21-2023

# ⚠️ ACTIVE DEVELOPMENT ⚠️ #
## ## ## ## ## ## ## ## ## ##

# 09-20-2023: Added function call handling; error handling; functional conversational context memory
# 09-21-2023: Added logging; added function call response handling; added session ID parameter to conversation history; added web search function

import os
import logging
import openai
import requests  # For web search

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
serp_api_key = "149b3d1e60ca9e74b11075800f583d32a70a4a426c6162c1b9a1f3f09dfd4efb"

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

        # Web search function call handling
        if "web_search" in assistant_reply:
            # Using the last user message as the query
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
