import os
import openai
from dotenv import load_dotenv
from pprint import pprint as print

load_dotenv()

openai.api_key = os.environ['OPEN_API_KEY']

def generate_ans(ques):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {
              "role": "system",
              "content": "You are a very knowledgeable and incredible AI that can answer any question uniquely."
            },
            {
                "role": "user",
                "content": f"Answer the question {ques}"
            }
        ]
    )
    return response["choices"][0]["message"]["content"]

ques = "Give innovative ideas which can Reinvent businesses and accelerate change with the power of technology."
response = generate_ans(ques)

print(response)



'''
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
