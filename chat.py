from openai import OpenAI

client = OpenAI(
   api_key='API-KEY'
 )
completion = client.chat.completions.create(
  model="text-embedding-ada-002",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)