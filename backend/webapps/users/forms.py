from typing import List, Optional
from fastapi import Request
from fastapi.param_functions import Depends


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None

    # unblock
    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.email = form.get("email")
        self.password = form.get("password")


    # validate data
    async def is_valid(self):
        # usernameがない場合、またはusernameが4文字以上ではない場合、エラー扱いとする
        if not self.username or not len(self.username) > 4:
            self.errors.append("Username must be > 4 chars")
        # emailがない場合、またはemailに＠がない場合、エラー扱いとする
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Valid email is required")
        # paswordがない場合、またはpasswordが5文字より大きくない場合、エラー扱いとする
        if not self.password or not len(self.password) > 5:
            self.errors.append("Password must be > 5 chars")

        # 上記3つのエラーが全くなければ、True返す
        if not self.errors:
            return True
        else:
            return False
        
