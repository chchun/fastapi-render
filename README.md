# FastAPI + PostgreSQL + Redis (Key‑Value) 예제

## 🚀 기능
- PostgreSQL `User` 테이블에 사용자 정보 저장
- Redis(Key‑Value)에 JSON 형태로 사용자 캐시 저장
- 캐시 우선 조회 후 DB 조회 및 캐싱

## ⚙️ 시스템 구성
| 구성 요소       | 역할 |
|----------------|------|
| PostgreSQL     | 영속적 데이터 저장 |
| Redis          | 빠른 조회를 위한 캐시 |
| FastAPI        | REST API 구현 |
| PyCharm (Windows) | 개발 환경 |

## 📁 프로젝트 구조

fastapi_redis/
├── .env
├── README.md
├── requirements.txt
├── database.py
├── models.py
├── schemas.py
├── keyvalue.py
└── main.py

shell
복사
편집

## 🔧 환경설정

### .env 파일 예시

DATABASE_URL=postgresql://username:password@localhost:5432/mydb
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

markdown
복사
편집

- PostgreSQL과 Redis 정보를 환경변수로 설정
- `.env` 파일을 `.gitignore`에 추가하세요!

## 📦 설치 및 실행

```bash
pip install -r requirements.txt
uvicorn main:app --reload
