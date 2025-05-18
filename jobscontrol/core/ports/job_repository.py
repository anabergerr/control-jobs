from abc import ABC, abstractmethod

from core.domain.job import JobCreate, JobResponse


class JobRepository(ABC):
    @abstractmethod
    def create_job(self, user_id: int, job: JobCreate) -> JobResponse:
        pass

    @abstractmethod
    def get_jobs(self, user_id: int) -> list[JobResponse]:
        pass

    @abstractmethod
    def get_job_by_id(self, user_id: int, job_id: int) -> JobResponse:
        pass

    @abstractmethod
    def update_job(self, user_id: int, job_id: int, job: JobCreate) -> JobResponse:
        pass

    @abstractmethod
    def delete_job(self, user_id: int, job_id: int):
        pass
