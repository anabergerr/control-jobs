from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Inicialize a SQLAlchemy (será configurada em app.py)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type_job = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Job {self.title}>'