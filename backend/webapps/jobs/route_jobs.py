from fastapi import APIRouter, requests
from fastapi import Request
from fastapi.params import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm.session import Session
from db.repository.jobs import list_jobs
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.jobs import retreive_job


template = Jinja2Templates(directory="templates")
# APIRouterのプロパティ「include_in_schema=False」で/docsにアクセスしたときのスキーマを非表示にできる
# これは、homepage.htmlがフロントエンドの分野であるため、非表示にしています。
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request:Request, db:Session=Depends(get_db), msg:str=None):
    jobs = list_jobs(db=db)
    # print(dir(requests))
    return template.TemplateResponse("jobs/homepage.html", {"request":request, "jobs":jobs, "msg":msg})

@router.get("/detail/{id}")
def job_detail_by_id(id:int, request:Request, db:Session=Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return template.TemplateResponse("jobs/detail.html", {"request":request, "job":job})