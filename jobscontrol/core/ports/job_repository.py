from abc import ABC, abstractmethod

from core.domain.job import JobCreate, JobResponse  # Importe as classes corretas


class JobRepository(ABC):
    @abstractmethod
    def create_job(self, job: JobCreate) -> JobResponse:
        pass

    @abstractmethod
    def get_jobs(self) -> list[JobResponse]:
        pass

    @abstractmethod
    def get_job_by_id(self, job_id: int) -> JobResponse:
        pass

    @abstractmethod
    def update_job(self, job_id: int, job: JobCreate) -> JobResponse:
        pass

    @abstractmethod
    def delete_job(self, job_id: int):
        pass
