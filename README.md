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

## 📁 프로젝트 구조

fastapi_redis/
├── .env
├── README.md
├── requirements.txt
├── keyvalue.py
└── main.py


## 🔧 환경변수 설정

### `.env` 예시
REDIS_URL=redis://red-xxxxxxxxxxxx:6379

- Render Key‑Value 인스턴스의 **Internal URL** 복사 후 `REDIS_URL` 환경변수에 설정
- 외부 접속이 필요할 경우 `rediss://` URL 사용하고 IP 화이트리스트를 설정해야 합니다 :contentRe
