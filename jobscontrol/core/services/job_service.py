from core.domain.job import JobCreate
from core.ports.job_repository import JobRepository


class JobService:
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    def create_job(self, user_id: int, job: JobCreate):
        return self.job_repository.create_job(user_id, job)

    def get_jobs(self, user_id: int):
        return self.job_repository.get_jobs(user_id)

    def get_job_by_id(self, user_id: int, job_id: int):
        return self.job_repository.get_job_by_id(user_id, job_id)

    def update_job(self, user_id: int, job_id: int, job: JobCreate):
        return self.job_repository.update_job(user_id, job_id, job)

    def delete_job(self, user_id: int, job_id: int):
        return self.job_repository.delete_job(user_id, job_id)
