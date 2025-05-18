from datetime import datetime

from pydantic import BaseModel


class JobCreate(BaseModel):
    name_job: str
    sequence_job: str
    name_company: str
    result_job: str
    obs_job: str | None = None


class JobResponse(BaseModel):
    id: int
    name_job: str
    sequence_job: str
    name_company: str
    result_job: str
    obs_job: str | None = None
    date: datetime | None = None
    user_id: int

    model_config = {"from_attributes": True}
