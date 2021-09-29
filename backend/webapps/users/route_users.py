from fastapi import APIRouter
from fastapi.exceptions import FastAPIError
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get("/register/")
def register(request: Request):
    return templates.TemplateResponse("users/register.html", {"request": request})
