from openai import OpenAI

client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key="sk-####")

model_a = "openai/gpt-oss-120b"

model_a_msg = [{
    "role":"system",
    "content":"You are Alex and expert in java language, ask a simple one liner question on java"
}]

def ask_question():
    qtn = client.chat.completions.create(
        model=model_a,
        messages=model_a_msg
    )
    return qtn.choices[0].message.content

def answer_question(q):
    qtn = client.chat.completions.create(
        model=model_a,
        messages=[{
            "role":"user",
            "content":f"""You are a recently graduated software engineer and has studied Java language during academics and can give answers a question {q} in one line"""}]
    )
    return qtn.choices[0].message.content

def validate_Answer(q,a):
    qtn = client.chat.completions.create(
        model=model_a,
        messages=[{
            "role":"user",
            "content":f"""You are an expert Java software engineer who has question {q} and answer {a} and says only yes if answer is correct else only no"""}]
    )
    return qtn.choices[0].message.content

for i in range(5):
    q = ask_question()
    print(f"Question: {q}\n")
    a = answer_question(q)
    print(f"Answer: {a}\n")
    verdict = validate_Answer(q,a)
    print(f"verdict: {verdict}")


