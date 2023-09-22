# OpenAI API <!-- omit from toc -->

_Current OpenAI API documentation._

**Updated:** 09-20-2023

---

## GPT Models

| Model               | Description                                                                               | Max Tokens    | Training Data  |
| ------------------- | ----------------------------------------------------------------------------------------- | ------------- | -------------- |
| `gpt-4`             | More capable than any GPT-3.5 model, able to do more complex tasks, & optimized for chat. | 8,196 tokens  | Up to Sep 2021 |
| `gpt-4-32k`         | Same capabilities as the standard gpt-4 mode but with 4x the context length.              | 32,768 tokens | Up to Sep 2021 |
| `gpt-3.5-turbo`     | Most capable GPT-3.5 model & optimized for chat at 1/10th the cost of `text-davinci-003`. | 4,097 tokens  | Up to Sep 2021 |
| `gpt-3.5-turbo-16k` | Same capabilities as the standard gpt-3.5-turbo model but with 4 times the context.       | 16,385 tokens | Up to Sep 2021 |

---

## Chat completions API endpoint

The latest models are accessed through the chat completions API endpoint:

| MODELS                                                     | API ENDPOINT                                 |
| ---------------------------------------------------------- | -------------------------------------------- |
| `gpt-4`, `gpt-4-32k`, `gpt-3.5-turbo`, `gpt-3.5-turbo-16k` | <https://api.openai.com/v1/chat/completions> |

---

## Request Example

```json
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
```

This queries the `gpt-3.5-turbo` model to complete the text. Response should resemble the following:

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "gpt-3.5-turbo-0613",
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 7,
    "total_tokens": 20
  },
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "\n\nThis is a test!"
      },
      "finish_reason": "stop",
      "index": 0
    }
  ]
}
```

Let's break down the `response` object. We can see the `finish_reason` is `stop`, which means the API returned the full chat completion generated by the model without running into any limits. In the `choices` list, we only generated a single message, but you can set the `n` parameter to generate multiple messages choices.

---

## Chat completions

Chat models take list of messages as input & return model-generated message as output.

### `messages` parameter

The main input is the `messages` parameter. Messages must be an array of message objects where each object has a `role` (either `system`, `user`, or `assistant`) & `content`. Conversations can be as short as one message or contain long back & forth turns.

#### `system` messages

Conversations are usually formatted with a `system` message first, followed by alternating `user` & `assistant` messages.

The `system` message helps set the assistant's behavior. You can modify the assistant's personality or provide specific instructions about how it should behave throughout the conversation. Note that the `system` message is optional; without a `system` message, the model's behavior will be similar to a generic message like "You are a helpful assistant."

#### `user` messages

`user` messages provide requests or comments for the assistant to respond to.

#### `assistant` messages

`assistant` messages store previous assistant responses. `assistant` messages can also be written by you to give examples of desired behavior.

### Examples

```py
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

Including conversation history is important when user instructions refer to prior messages. In the example above, the final question ("Where was it played?") only makes sense in the context of the prior messages about the World Series of 2020.

Models have no memory of past requests, so all relevant information must be supplied as part of the conversation history in each request. If a conversation exceeds the token limit, it will need to be shortened.

#### Example Response

_Example Chat completions API response._

```py
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      }
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
```

_The assistant’s reply can be extracted with:_

```py
response['choices'][0]['message']['content']
```

---

### `finish_reason` property

Every `response` will include the `finish_reason` property. Possible values for `finish_reason` are:

- `stop`: Returns complete message or message terminated by `stop` sequence
- `length`: Model exceeds token limit or `max_tokens` parameter
- `function_call`: Model calls a function
- `content_filter`: Omitted content due to flag from content filters
- `null`: Response still in progress or incomplete

---

### Chat completion object

_Represents chat completion response returned by model based on input._

**Chat completion parameters:**

| Parameter | Data type | Details                                                |
| --------- | --------- | ------------------------------------------------------ |
| `id`      | `str`     | Unique ID for chat completion                          |
| `object`  | `str`     | Object type: always `chat.completion`                  |
| `created` | `int`     | When chat completion was created                       |
| `model`   | `str`     | Model used for chat completion                         |
| `choices` | `array`   | List of chat completion choices; can be >1 if `n` = >1 |
| `usage`   | `object`  | Usage statistics for completion request                |

#### Parameter properties

**`choices` parameter:**

| Property        | Data type | Details                                        |
| --------------- | --------- | ---------------------------------------------- |
| `index`         | `int`     | Index of choice in list of choices             |
| `message`       | `object`  | Chat completion message generated by the model |
| `finish_reason` | `str`     | Reason the model stopped generating tokens     |

**Chat completion object example:**

```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "\n\nHello there, how may I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

**`message` object:**

| Property        | Data type   | Details                                           |
| --------------- | ----------- | ------------------------------------------------- |
| `role`          | `str`       | Message author                                    |
| `content`       | `str`, null | Message contents                                  |
| `function_call` | `object`    | Name & arguments for generated & called functions |

**`function_call` object:**

| Property    | Data type | Details                                                  |
| ----------- | --------- | -------------------------------------------------------- |
| `name`      | `str`     | Function name                                            |
| `arguments` | `str`     | Function arguments generated by the model in JSON format |

_Note that the model does not always generate valid JSON & may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function._

**`usage` object:**

Usage statistics for the completion request.

| Property            | Data type | Details                                                  |
| ------------------- | --------- | -------------------------------------------------------- |
| `prompt_tokens`     | `int`     | Prompt token number                                      |
| `completion_tokens` | `int`     | Generated completion number                              |
| `total_tokens`      | `int`     | Total token amount used in request (prompt + completion) |

---

### Chat completion `chunk` object

_Streamed chunk of returned response, based on provided input._

**`chunk` object parameters:**

| Parameter | Data type | Details                                                |
| --------- | --------- | ------------------------------------------------------ |
| `id`      | `str`     | Unique ID for chunk                                    |
| `object`  | `str`     | Object type: always `chat.completion.chunk`            |
| `created` | `int`     | When chunk was created                                 |
| `model`   | `str`     | Model used                                             |
| `choices` | `array`   | List of chat completion choices; can be >1 if `n` = >1 |

### Chat parameter properties

**`choices` object properties:**

_List of chat completion choices. Can be >1 if `n` is >1._

| Property        | Data type | Details                                    |
| --------------- | --------- | ------------------------------------------ |
| `index`         | `int`     | Index of choice in the list of choices     |
| `delta`         | `object`  | Chat completion message                    |
| `finish_reason` | `str`     | Reason the model stopped generating tokens |

**`delta` object properties:**

_Chat completion `delta` generated by streamed model responses._

| Property        | Data type   | Details                                           |
| --------------- | ----------- | ------------------------------------------------- |
| `role`          | `str`       | Role of message author                            |
| `content`       | `str`, null | Chunk message contents                            |
| `function_call` | `object`    | Name & arguments for generated & called functions |

**`function_call` object properties:**

_Name & arguments of function that should be called as generated by the model._

| Property    | Data type | Details                                                  |
| ----------- | --------- | -------------------------------------------------------- |
| `name`      | `str`     | Function name                                            |
| `arguments` | `str`     | Function arguments generated by the model in JSON format |

---

### Create chat completions

**`POST`:** <https://api.openai.com/v1/chat/completions>

_Creates model response for given chat conversation._

#### Create chat completions: Parameters

| Parameter           | Data type(s)         | Required    | Description                                                                      | Default          |
| ------------------- | -------------------- | ----------- | -------------------------------------------------------------------------------- | ---------------- |
| `messages`          | `array`              | yes         | List of conversation messages                                                    | n/a              |
| `functions`         | `array`              | yes         | List of functions that model generates                                           | n/a              |
| `function_call`     | `str`, undefined     | no          | Controls how model responds to function calls; see "NOTES" below                 | n/a              |
| `temperature`       | number, null         | see "NOTES" | Sampling temperature; alternative to `top_p`                                     | Default: `1`     |
| `top_p`             | number, null         | see "NOTES" | Nucleus sampling; alternative to `temperature`                                   | Default: `1`     |
| `n`                 | `int`, null          | no          | Amount of completion choices to generate for each input                          | Default: `1`     |
| `stream`            | `bool`, null         | no          | If `True`, partial message deltas will be sent                                   | Default: `False` |
| `stop`              | `str`, `array`, null | no          | Up to 4 sequences where API will stop generating further tokens                  | Default: `null`  |
| `max_tokens`        | `int`, null          | no          | Max token amount to generate in chat completion; see "NOTES" below               | Default: `inf`   |
| `presence_penalty`  | number, null         | no          | Positive values increase likelihood to talk about new topics                     | Default: `0`     |
| `frequency_penalty` | number, null         | no          | Positive values decrease likelihood to repeat same line verbatim                 | Default: `0`     |
| `logit_bias`        | `map`                | no          | Modify likelihood of specified tokens appearing in completion; see "NOTES" below | Default: `null`  |
| `user`              | `str`                | no          | Unique ID for end-user which can help OpenAI detect abuse                        | n/a              |

**NOTES:**

- Use `temperature` or `top_p` property, not both
- `temperature`: Set between 0 & 2; higher values are more random; lower values are more focused
- `top_p`: Nucleus sampling: the model considers the results of tokens with `top_p` probability mass (so value of `0.1` means only the tokens comprising the top 10% probability mass are considered)
- `function_call`: `none` means model doesn't call a function & responds to end-user; `auto` means model can pick between an end-user or calling a function; coding a specific function via `{"name":\ "my_function"}` forces model to call that function; `none` is default if no functions are present; `auto` is default if functions are present
- `stream`: Tokens will be sent as data-only server-sent events as they become available with stream terminated by a `data: [DONE]` message
- `logit_bias`: Accepts `json` object that maps tokens (specified by token ID in the tokenizer) to associated bias value between -100 & 100; mathematically, the bias is added to the logits generated by the model prior to sampling; values between -1 & 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token
- `max_tokens`: Remember the **total** length of input tokens & generated tokens is limited by model context length
- `presence_penalty` & `frequency_penalty`: Value must be between -2.0 & 2.0

#### Example requests

```py
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=True
)

for chunk in completion:
  print(chunk.choices[0].delta)
```

_Response:_

```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "Hello"
      },
      "finish_reason": "stop"
    }
  ]
}
```

---

## Function calling

You can describe functions to `gpt-3.5-turbo`/`gpt-4` (and their variants) & have the model intelligently choose to output a JSON object containing arguments to call those functions. The Chat completions API does not call the function; instead, the model generates JSON that you can use to call the function in your code.

Functions count against the model's context limit. If running into context limits, we suggest limiting the number of functions or the length of documentation you provide for function parameters.

### Function calling steps

_Basic steps for function calling:_

1. Call model with user query & function set defined in the functions parameter
2. The model can choose to call a function; if so, the content will be a stringified JSON object adhering to our custom schema
3. Parse string into JSON in our code & call function with the provided arguments (if they exist)
4. Call model again by appending function response as new message & let model summarize results back to the user

### Function calling use cases

- Create chatbots that answer questions by calling external APIs
  - define functions like `send_email(to: string, body: string)` or `get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')`
- Convert natural language into API calls
  - convert "Who are my top customers?" to `get_customers(min_revenue: int, created_before: string, limit: int)` and call your internal API
- Extract structured data from text
  - define a function called `extract_data(name: string, birthday: string)`, or `sql_query(query: string)`

_The steps for function calling in action can be seen in this example:_

```py
import openai
import json

# Example dummy function hardcoded to return the same weather
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

def run_conversation():
    # Step 1: send conversation & available functions to GPT
    messages = [{"role": "user", "content": "What's the weather like in Boston?"}]
    functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
   "location": {
       "type": "string",
       "description": "The city and state, e.g. San Francisco, CA",
   },
   "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default but we'll be explicit
    )
    response_message = response["choices"][0]["message"]

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )

        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        return second_response

print(run_conversation())
```

In the example above, we sent the function response back to the model and let it decide the next step. It responded with a user-facing message which was telling the user the temperature in Boston, but depending on the query, it may choose to call a function again. For example, if you ask the model “Find the weather in Boston this weekend, book dinner for two on Saturday, and update my calendar” and provide the corresponding functions for these queries, it may choose to call them back to back and only at the end create a user-facing message.

If you want to force the model to call a specific function you can do so by setting `function_call: {"name": "<insert-function-name>"}`. You can also force the model to generate a user-facing message by setting function_call: "none". Note that the default behavior (`function_call: "auto"`) is for the model to decide on its own whether to call a function and if so which function to call.

The response format is similar to the response format of the Chat completions API but also includes the optional field `logprobs`.

Hallucinated outputs in function calls can often be mitigated with a `system` message. For example, if you find that a model is generating function calls with functions that weren't provided to it, try using a `system` message that says: "Only use the functions you have been provided with."

---

---