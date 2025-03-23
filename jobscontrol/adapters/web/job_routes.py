from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from adapters.persistence.job_repository_impl import JobRepositoryImpl
from core.domain.job import JobCreate, JobResponse  # Importe as classes corretas
from core.services.job_service import JobService
from database.database import SessionLocal

router = APIRouter()


# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/jobs/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    job_service = JobService(JobRepositoryImpl(db))
    return job_service.create_job(job)


@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    job_service = JobService(JobRepositoryImpl(db))
    return job_service.get_jobs()


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
