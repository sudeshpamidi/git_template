from openai import OpenAI
import os

print(os.getenv("OPENAI_API_KEY"))
client = OpenAI(
   api_key= os.getenv("OPENAI_API_KEY") )
completion = client.chat.completions.create(
  model="text-embedding-ada-002",
  messages=[
    {"role": "system", "content": "Write a python script to print 'hello world'."}    
  ]
)

output = completion.choices[0]["text"]
print(output)
with open("output.py","w") as file:
    file.write(output)
