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

from schemas.jobs import JobCreate
from fastapi import responses, status
from fastapi.security.utils import get_authorization_scheme_param
 
from db.models.users import User
from db.repository.jobs import create_new_job  
from apis.version1.route_login import get_current_user_from_token
from webapps.jobs.forms import JobCreateForm


templates = Jinja2Templates(directory="templates")
# APIRouterのプロパティ「include_in_schema=False」で/docsにアクセスしたときのスキーマを非表示にできる
# これは、homepage.htmlがフロントエンドの分野であるため、非表示にしています。
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request:Request, db:Session=Depends(get_db), msg:str=None):
    jobs = list_jobs(db=db)
    # print(dir(requests))
    return templates.TemplateResponse("jobs/homepage.html", {"request":request, "jobs":jobs, "msg":msg})

@router.get("/detail/{id}")
def job_detail_by_id(id:int, request:Request, db:Session=Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return templates.TemplateResponse("jobs/detail.html", {"request":request, "job":job})

@router.get("/post-a-job/")  
def create_job(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("jobs/create_job.html", {"request": request})
 
 
@router.post("/post-a-job/")
async def create_job(request: Request, db: Session = Depends(get_db)):
    form = JobCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)
            job = JobCreate(**form.__dict__)
            job = create_new_job(job=job, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/detail/{job.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("jobs/create_job.html", form.__dict__)
    return templates.TemplateResponse("jobs/create_job.html", form.__dict__)