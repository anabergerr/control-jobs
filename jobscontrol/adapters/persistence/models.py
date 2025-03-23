from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from database.database import Base  # Importando a base correta


class Job(Base):
    __tablename__ = "jobs"

    id_job = Column(Integer, primary_key=True, index=True)
    name_job = Column(String(100), nullable=False)
    sequence_job = Column(String(100), nullable=False)
    name_company = Column(String(100), nullable=False)
    result_job = Column(String(100), nullable=False)
    obs_job = Column(String(600), nullable=True)
    date = Column(DateTime, default=datetime.utcnow)

    def as_dict(self):
        return {
            "id_job": self.id_job,
            "name_job": self.name_job,
            "sequence_job": self.sequence_job,
            "name_company": self.name_company,
            "result_job": self.result_job,
            "obs_job": self.obs_job,
            "date": self.date.isoformat() if self.date else None,
        }
