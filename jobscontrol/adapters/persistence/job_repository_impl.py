from sqlalchemy.orm import Session

from adapters.persistence.models import Job
from core.domain.job import JobCreate, JobResponse
from core.ports.job_repository import JobRepository


class JobRepositoryImpl(JobRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_job(self, job: JobCreate) -> JobResponse:
        db_job = Job(**job.model_dump())
        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)
        return JobResponse.model_validate(db_job)

    def get_jobs(self) -> list[JobResponse]:
        jobs = self.db.query(Job).all()
        return [JobResponse.model_validate(job) for job in jobs]

    def get_job_by_id(self, job_id: int) -> JobResponse:
        job = self.db.query(Job).filter(Job.id_job == job_id).first()
        if job:
            return JobResponse.model_validate(job)
        return None

    def update_job(self, job_id: int, job: JobCreate) -> JobResponse:
        db_job = self.db.query(Job).filter(Job.id_job == job_id).first()
        for key, value in job.model_dump().items():
            setattr(db_job, key, value)
        self.db.commit()
        self.db.refresh(db_job)
        return JobResponse.model_validate(db_job)

    def delete_job(self, job_id: int):
        db_job = self.db.query(Job).filter(Job.id_job == job_id).first()
        self.db.delete(db_job)
        self.db.commit()
