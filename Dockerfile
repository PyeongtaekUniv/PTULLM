# Flask 애플리케이션을 위한 Dockerfile
FROM python:3.8-slim

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt ./

# Python 의존성 설치
RUN pip install -r requirements.txt

# 현재 디렉터리의 모든 파일을 컨테이너의 작업 디렉터리로 복사
COPY . .

# Gunicorn으로 Flask 앱 실행
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]