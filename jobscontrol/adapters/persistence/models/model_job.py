from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id_job = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name_job = Column(String(100), nullable=False)
    sequence_job = Column(String(100), nullable=False)
    name_company = Column(String(100), nullable=False)
    result_job = Column(String(100), nullable=False)
    obs_job = Column(String(600), nullable=True)
    date = Column(DateTime, default=lambda: datetime.now(UTC))

    user = relationship("User", back_populates="jobs")
