import openai
import os
from weather import temp
from weather import humid
from weather import wind

#class open():
openai.api_key = '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'
question = f'기온은 {temp}이고, 습도는 {humid}이고, 풍속은 {wind}일 때 뭐먹을지 추천해줘'

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role" : "user", "content" : question}
    ]
)

#print(completion.choices[0].message.content)
result = completion.choices[0].message.content
