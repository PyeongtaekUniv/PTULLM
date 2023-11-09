from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from answer import return_answer
import os

app = Flask(__name__)
CORS(app)

# 환경 변수에서 데이터베이스 설정 읽기
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# SQLAlchemy 데이터베이스 URI 구성
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 여기서 모델을 정의합니다. 예를 들어:
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    ip_address = db.Column(db.String(100))  # IP 주소를 저장할 새로운 필드

    def __init__(self, question, answer, ip_address):
        self.question = question
        self.answer = answer
        self.ip_address = ip_address


@app.route('/get-answer', methods=['POST'])
def get_answer():
    data = request.json
    question = data.get('question', '')

    # 이 함수는 return_answer 모듈에서 정의된 것으로 가정합니다.
    answer_dict = return_answer(question)
    answer_text = answer_dict.get('result')
    
    # X-Forwarded-For 헤더에서 IP를 얻습니다.
    # 이 헤더는 쉼표로 구분된 IP 주소 목록을 포함할 수 있습니다.
    # 실제 클라이언트 IP는 헤더의 맨 처음 부분에 있습니다.
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.remote_addr or 'Not Available'

    # 데이터베이스에 질문, 답변, IP 주소 저장
    new_entry = Answer(question=question, answer=answer_text, ip_address=ip_address)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'answer': {'result': answer_text}})




if __name__ == '__main__':
    db.create_all()  # 데이터베이스 테이블 생성
    app.run(host="0.0.0.0", port=5000, debug=True)
