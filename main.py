import openai
import tkinter as tk
import os
from config import *
from weather import temp
from weather import humid
from weather import wind


openai.api_key = open_api_key
question = f'기온은 {temp}이고, 습도는 {humid}이고, 풍속은 {wind}일 때 뭐먹을지 추천해줘'

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role" : "user", "content" : question}
    ]
)

print(completion.choices[0].message.content)
result = completion.choices[0].message.content # 문자열 저장

def show():
    lb.configure(text=result)
    what_btn.destroy()

def close():
    window.destroy()

window = tk.Tk()
window.geometry('1200x300')
window.title('오늘 뭐 먹지')

lb = tk.Label(window, text='오늘 뭐 먹지')
lb.pack()

what_btn = tk.Button(window, text="오늘 뭐 먹지", command=show, width = 20)
what_btn.pack()

close_btn = tk.Button(window, text='닫기', command=close, width = 20)
close_btn.pack()

window.mainloop()
