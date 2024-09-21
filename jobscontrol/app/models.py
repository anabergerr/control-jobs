from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Job(db.Model):
    id_job = db.Column(db.Integer, primary_key=True)
    name_job = db.Column(db.String(100), nullable=False)
    sequence_job = db.Column(db.String(100), nullable=False)
    name_company = db.Column(db.String(100), nullable=False)
    result_job = db.Column(db.String(100), nullable=False)
    obs_job = db.Column(db.String(600), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Job {self.name}>'

    def as_dict(self):
        return {
            'idJob': self.idJob,
            'name_job': self.name_job,
            'sequence_job': self.sequence_job,
            'name_company': self.name_company,
            'result_job': self.result_job,
            'obs_job': self.obs_job,
            'date': self.date.isoformat(),
        }
