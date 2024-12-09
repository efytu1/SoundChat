from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Describe the sentiment of this sentence with one of (high positive, low positive, high negative, low negative) : What is your name?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)