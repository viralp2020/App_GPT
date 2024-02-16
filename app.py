# main_app.py

import openai
from flask import Flask, render_template, request, jsonify
from config import OPENAI_API_KEY

# Set the OpenAI API key from the configuration
openai.api_key = OPENAI_API_KEY

# Create a Flask application
app = Flask(__name__)

# Initial message for the conversation, representing the system
messages = [{"role": "system", "content": "You are an expert that specializes in solving any kind of problems"}]

# Function to interact with the ChatGPT model
def CustomChatGPT(user_input):
    # Append user's message to the conversation
    messages.append({"role": "user", "content": user_input})
    
    # Use OpenAI API to get a response from the ChatGPT model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Extract the assistant's reply from the API response
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    
    # Append assistant's reply to the conversation
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    
    # Return the ChatGPT reply for further use
    return ChatGPT_reply

# Route to render the chat page
@app.route('/')
def chat_page():
    return render_template('chat_bot.html')

# Route to handle user input and get ChatGPT response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    response = CustomChatGPT(user_input)
    return jsonify({'response': response})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
