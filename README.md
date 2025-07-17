# 🔐 FastAPI + Render Key‑Value (Redis® 호환) 예제

## 🚀 기능
- FastAPI 서버리스 Web Service
- Render Key‑Value 인스턴스에서 사용자 정보 캐싱 (JSON 형태)
- 캐시 우선 조회 후 없으면 기본 데이터 생성 혹은 404 응답

## ⚙️ 시스템 구성
| 구성 요소       | 역할 |
|----------------|------|
| Render Web Service | FastAPI 앱 실행 (무료 웹 서비스, 최대 750시간/月) :contentReference[oaicite:1]{index=1} |
| Render Key‑Value    | Redis 호환 인메모리 캐시 (무료 인스턴스 제공) :contentReference[oaicite:2]{index=2} |
| PyCharm (Windows)   | 로컬 개발 환경 (환경 변수, 디버깅 지원) |

```plaintext
## 📁 프로젝트 구조

fastapi_redis/
├── .env
├── README.md
├── requirements.txt
├── keyvalue.py
└── main.py

```

## 🔧 환경변수 설정

### `.env` 예시
REDIS_URL=redis://red-xxxxxxxxxxxx:6379

- Render Key‑Value 인스턴스의 **Internal URL** 복사 후 `REDIS_URL` 환경변수에 설정
- 외부 접속이 필요할 경우 `rediss://` URL 사용하고 IP 화이트리스트를 설정해야 합니다 :contentRe


## 🔧 설치
```bash
pip install -r requirements.txt
🔗 환경변수 설정
.env 또는 Render Dashboard → Environment 탭에:

ini

REDIS_URL=redis://red-xxxxxxxxxxxx:6379
🚀 실행
'''bash
uvicorn main:app --host 0.0.0.0 --port $PORT --reload
'''

🧪 API 예시
POST /user/
bash
복사
편집
curl -X POST "https://<YOUR_APP_URL>/user/" \
  -H "Content-Type: application/json" \
  -d '{"id":"alice01","name":"Alice","grade":"A","phone":"010-1234-5678","kakao_use":true}'
응답:

json
복사
편집
{"status":"created","user":{"id":"alice01",...}}
GET /user/{id}
bash
복사
편집
curl "https://<YOUR_APP_URL>/user/alice01"
응답:

json
복사
편집
{"source":"cache","user":{"id":"alice01",...}}
🔧 배포 (Render.com Web Service)
GitHub에 코드 푸시

Render Dashboard → New → Web Service

리포 연결 후 Free plan 선택

Build: pip install -r requirements.txt

Start: uvicorn main:app --host 0.0.0.0 --port $PORT

Environment에 REDIS_URL 설정 (Key‑Value 내부 URL)

배포 후 API 테스트 (/user/..., /docs 확인)
