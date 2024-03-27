'''
https://platform.openai.com/docs/api-reference/streaming
'''

from openai import OpenAI
import openai

client = OpenAI(
        api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        base_url="https://api.953959.xyz/v1"
    )

completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You are here to help me with my day."},
                {"role": "user", "content": "Hello, Who are you?"},
            ],
            stream=True
        )

# Streaming
for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# If no streaming
# set client.chat.completions.create(stream=False) and than
# print(completion.choices[0].delta.content)