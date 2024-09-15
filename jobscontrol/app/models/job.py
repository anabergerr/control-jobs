from sqlalchemy import Enum
from app.extensions import db

class Job(db.Model):
    """Modelo de Job."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type_job = db.Column(db.String(50), nullable=False)

    YES = 'Yes'
    NO = 'No'
    COMPANY_RETURN_CHOICES = Enum('Yes', 'No', name='company_return_enum')  # Use Enum
    company_return = db.Column(
        COMPANY_RETURN_CHOICES,  # Use a Enum como tipo da coluna
        nullable=False,
        default=NO
    )
    date = db.Column(db.Date, nullable=False, default=db.func.current_date())

    def __repr__(self):
        return f"<Job {self.title}>"