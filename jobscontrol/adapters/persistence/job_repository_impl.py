from sqlalchemy.orm import Session
from core.domain.job import JobCreate, JobResponse  # Importe as classes corretas
from core.ports.job_repository import JobRepository
from database.database import Base

class JobRepositoryImpl(JobRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_job(self, job: JobCreate) -> JobResponse:
        db_job = Base(**job.dict())
        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)
        return JobResponse.from_orm(db_job)

    def get_jobs(self) -> list[JobResponse]:
        jobs = self.db.query(Base).all()
        return [JobResponse.from_orm(job) for job in jobs]

    def get_job_by_id(self, job_id: int) -> JobResponse:
        job = self.db.query(Base).filter(Base.id_job == job_id).first()
        if job:
            return JobResponse.from_orm(job)
        return None

    def update_job(self, job_id: int, job: JobCreate) -> JobResponse:
        db_job = self.db.query(Base).filter(Base.id_job == job_id).first()
        for key, value in job.dict().items():
            setattr(db_job, key, value)
        self.db.commit()
        self.db.refresh(db_job)
        return JobResponse.from_orm(db_job)

    def delete_job(self, job_id: int):
        db_job = self.db.query(Base).filter(Base.id_job == job_id).first()
        self.db.delete(db_job)
        self.db.commit()