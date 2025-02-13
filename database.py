import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Render 내부 DB URL (환경 변수)
INTERNAL_DB_URL = os.getenv("DATABASE_URL")

# 🔹 외부 DB URL을 직접 소스 코드에서 설정 (여기에 Render External DB URL 입력)
EXTERNAL_DB_URL = "postgresql://mcandle:ng7aDt9WTfo2nXfzm2YKMmWjF66lpRsh@dpg-cumkujd6l47c7394obug-a.singapore-postgres.render.com/mcandle_db"

# 환경변수 대신 외부 DB URL을 기본값으로 사용 (내부 DB URL이 있으면 내부 사용)
DATABASE_URL = INTERNAL_DB_URL if INTERNAL_DB_URL else EXTERNAL_DB_URL

# 예외 처리: DATABASE_URL이 설정되지 않았을 경우
if not DATABASE_URL:
    raise ValueError("DATABASE_URL이 설정되지 않았습니다.")

# 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()