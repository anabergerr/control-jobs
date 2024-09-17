from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    idJob = db.Column(db.Integer, primary_key=True)
    name_job = db.Column(db.String(100), nullable=False)
    sequence_job = db.Column(db.String(100), nullable=False)
    name_company = db.Column(db.String(100), nullable=False)
    result_job = db.Column(db.String(100), nullable=False)
    obs_job = db.Column(db.String(600), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Job {self.name}>'
