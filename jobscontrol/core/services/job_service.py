from core.domain.job import JobCreate, JobResponse  # Importe as classes corretas
from core.ports.job_repository import JobRepository


class JobService:
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    def create_job(self, job: JobCreate) -> JobResponse:
        return self.job_repository.create_job(job)

    def get_jobs(self) -> list[JobResponse]:
        return self.job_repository.get_jobs()

    def get_job_by_id(self, job_id: int) -> JobResponse:
        return self.job_repository.get_job_by_id(job_id)

    def update_job(self, job_id: int, job: JobCreate) -> JobResponse:
        return self.job_repository.update_job(job_id, job)

    def delete_job(self, job_id: int):
        return self.job_repository.delete_job(job_id)
