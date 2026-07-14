from openai import OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="Ollama")

while True:
    userInput = input("Ask a Question or Press E for exit?")

    if userInput !="E":
        while True:
            res = openai.chat.completions.create(
                model="qwen2:7b",
                messages=[{
                    "role":"user",
                    "content": userInput
                }])
            
            print(res.choices[0].message.content)
    else:
        exit       
