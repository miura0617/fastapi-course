from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# /docsにアクセスしてAPIを動作させたときにserver responseにパスワードを非表示にしてセキュリティ対策
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        # 戻り地をdict型に変換するため
        orm_mode = True