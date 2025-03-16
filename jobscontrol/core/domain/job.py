from pydantic import BaseModel
from datetime import datetime

class JobCreate(BaseModel):
    name_job: str
    sequence_job: str
    name_company: str
    result_job: str
    obs_job: str | None = None

class JobResponse(BaseModel):
    id_job: int
    name_job: str
    sequence_job: str
    name_company: str
    result_job: str
    obs_job: str | None = None
    date: datetime | None = None

    class Config:
        from_attributes = True
