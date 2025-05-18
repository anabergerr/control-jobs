import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from adapters.persistence.job_repository_impl import JobRepositoryImpl
from core.domain.job import JobCreate, JobResponse
from core.services.job_service import JobService
from database.database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
load_dotenv()
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"


router = APIRouter()


def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    print("TOKEN RECEBIDO:", token)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD:", payload)
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(status_code=401, detail="User ID not found")
        return user_id
    except JWTError as e:
        print("ERRO JWT:", e)
        raise HTTPException(status_code=401, detail="Invalid token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/jobs/", response_model=JobResponse)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
):
    print("akiii", user_id)
    job_service = JobService(JobRepositoryImpl(db))
    return job_service.create_job(user_id, job)


@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(
    db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)
):
    job_service = JobService(JobRepositoryImpl(db))

    return job_service.get_jobs(user_id)


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job_service = JobService(JobRepositoryImpl(db))
    job = job_service.get_job_by_id(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.put("/jobs/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job: JobCreate, db: Session = Depends(get_db)):
    job_service = JobService(JobRepositoryImpl(db))
    return job_service.update_job(job_id, job)


@router.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job_service = JobService(JobRepositoryImpl(db))
    job_service.delete_job(job_id)
    return {"message": "Job deleted successfully"}
