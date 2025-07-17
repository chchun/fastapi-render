import os
import json
from typing import Optional
from redis import from_url
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL 환경변수가 필요합니다.")

redis_client = from_url(REDIS_URL, decode_responses=True)

# 사용자 데이터 모델
class UserModel(BaseModel):
    id: str
    name: str
    grade: str
    phone: str
    kakao_use: bool

# 1) UserModel 기반 캐시 저장
def cache_user(user: UserModel) -> None:
    """
    UserModel 객체를 Redis에 JSON 형태로 저장합니다.
    Key: user:{id}
    """
    redis_client.set(f"user:{user.id}", user.json())

# 2) UserModel 기반 캐시 조회
def get_cached_user(user_id: str) -> Optional[UserModel]:
    """
    Redis에서 user:{user_id} 키로 JSON을 가져와 UserModel로 파싱합니다.
    캐시가 없으면 None 반환.
    """
    data = redis_client.get(f"user:{user_id}")
    if data:
        return UserModel.parse_raw(data)
    return None

# 3) 일반 문자열 key-value 저장
def set_key(key: str, value: str) -> bool:
    """
    일반 문자열 key-value 저장.
    성공 시 True, 실패 시 False 반환.
    """
    return redis_client.set(key, value)

# 4) 일반 문자열 key-value 조회
def get_key(key: str) -> Optional[str]:
    """
    일반 문자열 key-value 조회.
    키가 없으면 None 반환합니다.
    """
    return redis_client.get(key)
