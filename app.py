# main_app.py

import openai
from flask import Flask, render_template, request, jsonify
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)


messages = [{"role": "system", "content": "You are a  expert that specializes in Solving any kind of problems"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

@app.route('/')
def chat_page():
    return render_template('chat_bot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    response = CustomChatGPT(user_input)
    return jsonify({'response': response})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

