from fastapi import FastAPI, Form, Depends, Request, Query, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models.user import User
from starlette.responses import HTMLResponse, JSONResponse

app = FastAPI()

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 템플릿 & 정적 파일 설정
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# DB 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 서버 상태 확인 API
@app.get("/ping")
async def ping():
    return {"message": "Server is running!"}

# 🔹 사용자 조회 API
@app.get("/get", response_class=JSONResponse)
async def get_user(id: str = Query(..., description="사용자 ID"), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    
    return {
        "id": user.id,
        "name": user.name,
        "grade": user.grade,
        "phone": user.phone,
        "kakao_use": user.kakao_use,
        "member_card_no": user.member_card_no,
        "credit_card_name": user.credit_card_name,
        "credit_card_no": user.credit_card_no
    }

# 🔹 사용자 삭제 API
@app.delete("/delete")
async def delete_user(id: str = Query(..., description="삭제할 사용자 ID"), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    
    db.delete(user)
    db.commit()
    return {"message": f"사용자 {id}가 삭제되었습니다."}

# 🔹 사용자 입력 폼 페이지
@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# 🔹 사용자 정보 저장 (UPDATE 또는 INSERT)
@app.post("/submit")
async def submit_user(
    request: Request,
    id: str = Form(...),
    name: str = Form(...),
    grade: str = Form(...),
    phone: str = Form(...),
    kakao_use: str = Form(...),
    member_card_no: str = Form(...),
    credit_card_name: str = Form(...),
    credit_card_no: str = Form(...),
    db: Session = Depends(get_db)
):
    kakao_use_bool = kakao_use.lower() == "true"

    # 🔹 사용자 ID가 존재하는지 확인
    existing_user = db.query(User).filter(User.id == id).first()

    if existing_user:
        # 🔹 존재하면 UPDATE 수행
        existing_user.name = name
        existing_user.grade = grade
        existing_user.phone = phone
        existing_user.kakao_use = kakao_use_bool
        existing_user.member_card_no = member_card_no
        existing_user.credit_card_name = credit_card_name
        existing_user.credit_card_no = credit_card_no
    else:
        # 🔹 존재하지 않으면 INSERT 수행
        new_user = User(
            id=id,
            name=name,
            grade=grade,
            phone=phone,
            kakao_use=kakao_use_bool,
            member_card_no=member_card_no,
            credit_card_name=credit_card_name,
            credit_card_no=credit_card_no
        )
        db.add(new_user)

    db.commit()  # 🔹 UPDATE 또는 INSERT 후 커밋
    return templates.TemplateResponse("success.html", {"request": request, "name": name})
