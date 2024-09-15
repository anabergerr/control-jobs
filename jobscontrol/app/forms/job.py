from app.models.job import Job
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class JobForm(FlaskForm):
    """Formulário para criação de Job."""
    title = StringField('Título', validators=[DataRequired()])
    type_job = StringField('Tipo de Job', validators=[DataRequired()])
    company_return = SelectField('Retorno da Empresa', choices=[
        ('Yes', 'Sim'),
        ('No', 'Não'),
    ], validators=[DataRequired()])
    date = DateField('Data', validators=[DataRequired()])
    submit = SubmitField('Criar Job')

    def save(self):
        """Salva o Job no banco de dados."""
        job = Job(
            title=self.title.data,
            type_job=self.type_job.data,
            company_return=self.company_return.data,
            date=self.date.data
        )
        db.session.add(job)
        db.session.commit()
        return job