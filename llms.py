from openai import OpenAI
from together import Together
# from tenacity import retry, stop_after_attempt
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()


def openai_chat_fast_gen(input_prompt,
                         model_card='gpt-3.5-turbo',
                         temperature=0.7,
                         max_tokens=1024):

    assert (type(input_prompt) == str
            ), "openai api does not support batch inference."

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    message = [{"role": "user", "content": input_prompt}]

    response = client.chat.completions.create(
        model=model_card,
        messages=message,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )
    return response.choices[0].message.content


def togetherai_chat_fast_gen(input_prompt,
                             model_card='meta-llama/Llama-2-7b-hf',
                             temperature=0.7,
                             max_tokens=1000):

    assert (type(input_prompt) == str
            ), "You are trying to do batch inference. you sure?"

    client = Together(api_key=os.getenv('TOGETHERAI_API_KEY'))

    message = [{"role": "user", "content": input_prompt}]

    response = client.chat.completions.create(
        model=model_card,
        messages=message,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def anthropicai_fast_gen(input_prompt,
                         model_card='claude-3-sonnet-20240229',
                         temperature=0.7,
                         max_tokens=1000):

    assert (type(input_prompt) == str
            ), "You are trying to do batch inference. you sure?"

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=os.getenv('ANTHROPIC_API_KEY'),
    )

    message = [{"role": "user", "content": input_prompt}]

    response = client.messages.create(
        model=model_card,
        messages=message,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.content[0].text
