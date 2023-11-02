from flask import Flask, request, jsonify
from flask_cors import CORS

from answer import return_answer  # 해당 스크립트의 이름을 your_script_name으로 변경해주세요

app = Flask(__name__)
CORS(app)

@app.route('/get-answer', methods=['POST'])
def get_answer():
    data = request.json
    question = data.get('question', '')
    answer = return_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(port=5000)
