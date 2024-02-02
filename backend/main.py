from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def home():
    return "Hello world"

@app.route('/api/user', methods=['POST'])
def add_user():
    form = request.get_json()
    
    return jsonify({'success': True, 'data' : form})

if __name__ == '__main__':
    app.run(debug=True)