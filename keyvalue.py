import os, json
from redis import from_url
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL 환경변수가 필요합니다.")

redis_client = from_url(REDIS_URL, decode_responses=True)

class UserModel(BaseModel):
    id: str
    name: str
    grade: str
    phone: str
    kakao_use: bool

def cache_user(user: UserModel):
    redis_client.set(f"user:{user.id}", user.json())

def get_cached_user(user_id: str) -> UserModel | None:
    data = redis_client.get(f"user:{user_id}")
    if data:
        return UserModel.parse_raw(data)
    return None
