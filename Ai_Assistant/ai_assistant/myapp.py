import os
import sys
from flask import Flask, request, jsonify

# Add the directory containing the Python script to the system path
script_dir = os.path.abspath(os.path.join(os.getcwd(), 'backend'))  # Adjusted path
sys.path.append(script_dir)

# Import your Python script (adjust the import path accordingly)
import backend.main1 as ai

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Assuming you want to serve your frontend index.html as the main page
    return app.send_static_file('index.html')

@app.route('/process_speech', methods=['POST'])
def process_speech():
    speech_input = request.get_json()['input']
    output = ai.process_speech(speech_input)
    return jsonify({'output': output})

if __name__ == '__main__':
    # Set the static folder to serve static files from 'frontend' folder
    app.static_folder = os.path.join(os.getcwd(), 'frontend')
    app.run()
