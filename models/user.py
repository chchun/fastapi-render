from sqlalchemy import Column, String, Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    grade = Column(String)
    phone = Column(String)
    kakao_use = Column(Boolean)

    # 추가된 필드
    member_card_no = Column(String, unique=True)  # 멤버십 카드 번호
    credit_card_name = Column(String)  # 신용카드 회사명
    credit_card_no = Column(String, unique=True)  # 신용카드 번호
