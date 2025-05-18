from sqlalchemy.orm import Session

from adapters.persistence.models.model_job import Job
from core.domain.job import JobCreate
from core.ports.job_repository import JobRepository


class JobRepositoryImpl(JobRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_job(self, user_id: int, job: JobCreate):
        db_job = Job(**job.dict(), user_id=user_id)
        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)
        return db_job

    def get_jobs(self, user_id: int):
        return self.db.query(Job).filter(Job.user_id == user_id).all()

    def get_job_by_id(self, user_id: int, job_id: int):
        return (
            self.db.query(Job)
            .filter(Job.id_job == job_id, Job.user_id == user_id)
            .first()
        )

    def update_job(self, user_id: int, job_id: int, job: JobCreate):
        db_job = self.get_job_by_id(user_id, job_id)
        if db_job is None:
            return None
        for key, value in job.dict().items():
            setattr(db_job, key, value)
        self.db.commit()
        self.db.refresh(db_job)
        return db_job

    def delete_job(self, user_id: int, job_id: int):
        db_job = self.get_job_by_id(user_id, job_id)
        if db_job is not None:
            self.db.delete(db_job)
            self.db.commit()
