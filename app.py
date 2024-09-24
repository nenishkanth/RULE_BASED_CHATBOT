from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "help" in user_input or "assist" in user_input:
        return "I'm here to help! What do you need assistance with?"
    elif "time" in user_input or "what time" in user_input:
        return "I can't tell the time, but you can check your device!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day."
    elif "name" in user_input:
        return "I am your friendly chatbot!"
    elif "weather" in user_input:
        return "I'm unable to check the weather, but you can find that info online!"
    elif "your purpose" in user_input or "what do you do" in user_input:
        return "I am here to chat and assist you with basic queries!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! I'm always here if you need me."
    elif "how are you" in user_input or "how are things" in user_input:
        return "I'm just a chatbot, but thank you for asking!"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "age" in user_input or "how old" in user_input:
        return "Age is just a number, but I was created not too long ago!"
    elif "color" in user_input:
        return "I don't see colors, but I think blue is calming!"
    elif "sports" in user_input:
        return "I'm not great at sports, but I can talk about them if you'd like!"
    elif "movie" in user_input:
        return "I love watching movies, especially science fiction!"
    elif "food" in user_input:
        return "I don't eat, but I hear pizza is everyone's favorite!"
    elif "location" in user_input or "where are you" in user_input:
        return "I'm right here, wherever you need me!"
    else:
        return "Sorry, I don't understand that. Can you try asking something else?"

# Route for the chatbot page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle user messages and return bot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
