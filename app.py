from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from answer import return_answer  # 해당 스크립트의 이름을 your_script_name으로 변경해주세요

import os

app = Flask(__name__)
CORS(app)

# 환경변수에서 MySQL 설정을 로드하여 데이터베이스 URI 구성
db_user = os.getenv('RDS_USERNAME')
db_password = os.getenv('RDS_PASSWORD')
db_host = os.getenv('RDS_HOSTNAME')
db_name = os.getenv('RDS_DB_NAME')
db_port = os.getenv('RDS_PORT', '3306')  # MySQL 기본 포트는 3306입니다

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500))
    answer = db.Column(db.String(5000))

    def __repr__(self):
        return f'<QuestionAnswer {self.question}>'

@app.route('/get-answer', methods=['POST'])
def get_answer():
    data = request.json
    question = data.get('question', '')
    answer = return_answer(question)

    new_entry = QuestionAnswer(question=question, answer=answer)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"answer": answer})

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
