from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate_text():
    if request.is_json:  
        data = request.get_json()
        if 'text' in data:
            text = data['text']
            target_language = data.get('target_language', 'en')  

            translator = Translator()
            translated_text = translator.translate(text, dest=target_language).text

            response = {'translation': translated_text}
            return jsonify(response), 200, {'Content-Type': 'application/json'}

    return jsonify({'error': 'Invalid request or missing "text" parameter'}), 400, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    server = app.run(debug=True)
    if server:
        print("Flask server is running.")
    else:
        print("Failed to start Flask server.")
