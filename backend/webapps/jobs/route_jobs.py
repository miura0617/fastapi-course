from fastapi import APIRouter, requests
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


template = Jinja2Templates(directory="templates")
# APIRouterのプロパティ「include_in_schema=False」で/docsにアクセスしたときのスキーマを非表示にできる
# これは、homepage.htmlがフロントエンドの分野であるため、非表示にしています。
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request:Request):
    print(dir(requests))
    return template.TemplateResponse("jobs/homepage.html", {"request":request})
