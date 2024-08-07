import json

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from conversation_context import ConversationContext

app = Flask(__name__)
CORS(app)
conversation_context = ConversationContext()


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


app.register_error_handler(HTTPException, handle_exception)


@app.route('/select_model', methods=['POST'])
def select_model():
    data = request.get_json()
    model = data['model']
    if model == 'Llama2' or model == 'mistral':
        return jsonify({"message": f"Model set to {model}", 'status': 'ok'}), 200

    else:
        return jsonify({'error': f'Invalid model selected {model}',
                        "message": "You can only select llama2 model or mistral "
                                   "model"}), 400


@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data['question']
    response = conversation_context.get_answer(question)
    return jsonify(response), 200


@app.route('/history', methods=['GET'])
def history():
    return jsonify(conversation_context.get_history()), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
