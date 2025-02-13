# 📂 FastAPI + PostgreSQL + Render 프로젝트 구조

```plaintext
fastapi-render/
│── 📂 templates/               # 🔹 HTML 템플릿 폴더 (Jinja2 사용)
│   ├── base.html               # 🔹 기본 레이아웃 파일
│   ├── form.html               # 🔹 사용자 입력 폼
│   ├── success.html            # 🔹 입력 성공 페이지
│
│── 📂 static/                  # 🔹 정적 파일 (CSS, JS, 이미지 등)
│   ├── styles.css              # 🔹 기본 스타일 (선택사항)
│
│── 📂 models/                  # 🔹 데이터베이스 모델 폴더
│   ├── user.py                 # 🔹 User 모델 정의 (SQLAlchemy)
│
│── database.py                 # 🔹 데이터베이스 연결 및 설정
│── main.py                     # 🔹 FastAPI 서버 및 API 엔드포인트
│── requirements.txt            # 🔹 프로젝트 종속 패키지 목록
│── start.sh                    # 🔹 Render에서 FastAPI 실행 스크립트
│── .gitignore                  # 🔹 Git에서 제외할 파일 목록
│── README.md                   # 🔹 프로젝트 설명 파일
