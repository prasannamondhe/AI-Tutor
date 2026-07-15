import os

from openai import OpenAI


openai = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.environ["OPENROUTER_API_KEY"])

res = openai.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role":"user",
            "content":"Who is Narendra Modi? explain in one line"
        }
    ])

print(res.choices[0].message.content)