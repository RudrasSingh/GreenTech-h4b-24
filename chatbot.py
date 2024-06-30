from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        # Here you can add more sophisticated logic or integrate with an NLP model
        response_message = generate_response(user_message)
        return jsonify({'response': response_message})
    return jsonify({'response': 'Sorry, I did not understand that.'})

def generate_response(message):
    # Simple logic for response generation
    if 'hello' in message.lower():
        return 'Hello! How can I help you today?'
    elif 'help' in message.lower():
        return 'Sure, what do you need help with?'
    else:
        return 'I am here to assist you with anything you need.'

if __name__ == '__main__':
    app.run(debug=True)
