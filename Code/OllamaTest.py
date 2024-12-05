from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Describe the sentiment of this sentence with one of (high positive, low positive, high negative, low negative) : I am having a great day',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)