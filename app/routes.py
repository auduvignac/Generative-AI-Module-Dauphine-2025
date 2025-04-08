from flask import Blueprint, request, render_template, jsonify
from app.services.rag_service import generate_response

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    answer = generate_response(user_input)
    return jsonify({'answer': answer})