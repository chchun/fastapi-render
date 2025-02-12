from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

# 🔹 하드코딩된 사용자 데이터
dummy_user = {
    "id": "11111111",
    "name": "홍길동",
    "grade": "VIP",
    "phone": "010-1234-5678",
    "kakao_use": True,
    "cards": [
        {
            "card_company": "Shinhan",
            "card_number": "1234-5678-9012-3456"
        },
        {
            "card_company": "Samsung",
            "card_number": "9876-5432-1098-7654"
        }
    ]
}


@app.get("/")
async def root():
    return {"message": "Hello from Railway & PyCharm!"}

@app.get("/ping")
async def ping():
    return {"message": "pong"}

# 🔹 GET: 사용자 정보 조회 (하드코딩된 데이터 반환)
@app.get("/get")
async def get_user(id: str = Query(..., description="사용자 ID")):
    if id == "11111111":  # 특정 ID에 대해서만 응답
        return dummy_user
    else:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
