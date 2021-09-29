from fastapi import APIRouter
from fastapi import responses
from fastapi import Request
from fastapi import status, Depends
from fastapi.exceptions import FastAPIError
from fastapi.templating import Jinja2Templates

from db.repository.users import create_new_user
from db.session import get_db
from schemas.users import UserCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from webapps.users.forms import UserCreateForm


router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get("/register/")
def register(request: Request):
    return templates.TemplateResponse("users/register.html", {"request": request})

@router.post("/register/")
async def register(request:Request, db:Session=Depends(get_db)):
    form = UserCreateForm(request=request)
    # formインスタンス内のusername, email, passwordをセット
    await form.load_data()
    # formインスタンス内のusername, email, passwordを検証
    if await form.is_valid():
        user = UserCreate(
            username=form.username,
            email=form.email,
            password=form.password
        )
        try:
            user = create_new_user(user=user, db=db)
            return responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
        except IntegrityError:
            # not unique
            # username or email already exists
            form.__dict__.get("errors").append("Dpuplicate username or email")
            return templates.TemplateResponse("users/register.html", form.__dict__)
    return templates.TemplateResponse("users/register.html", form.__dict__)
    