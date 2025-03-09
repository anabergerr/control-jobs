from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal  # Importação da sessão do banco de dados
from app.models import Job  # Importação do modelo Job

router = APIRouter()


# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rota para listar todos os jobs
@router.get("/jobs/")
def get_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    jobs = db.query(Job).offset(skip).limit(limit).all()
    return jobs


# Rota para obter um job por ID
@router.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id_job == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


# Rota para criar um novo job
@router.post("/jobs/")
def create_job(job_data: dict, db: Session = Depends(get_db)):

    if 'date' in job_data and isinstance(job_data['date'], str):
        job_data['date'] = datetime.fromisoformat(job_data['date'])  # Converte para datetime

    new_job = Job(**job_data)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return {
        "message": "Job created successfully!",
        "job": new_job.as_dict()
    }


# Rota para atualizar um job existente
@router.put("/jobs/{job_id}")
def update_job(job_id: int, job_data: dict, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id_job == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    for key, value in job_data.items():
        setattr(job, key, value)
    db.commit()
    db.refresh(job)
    return job


# Rota para deletar um job
@router.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id_job == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted."}


# Rota para atualizar parcialmente um job
@router.patch("/jobs/{job_id}")
def update_job_partial(job_id: int, job_data: dict, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id_job == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    # Atualiza apenas os campos fornecidos no payload
    for key, value in job_data.items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job
