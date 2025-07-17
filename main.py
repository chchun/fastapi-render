from fastapi import FastAPI, HTTPException
from keyvalue import cache_user, get_cached_user, UserModel

app = FastAPI()

@app.post("/user/")
def create_user(user: UserModel):
    cache_user(user)
    return {"status": "created", "user": user}

@app.get("/user/{user_id}")
def read_user(user_id: str):
    user = get_cached_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"source": "cache", "user": user}

