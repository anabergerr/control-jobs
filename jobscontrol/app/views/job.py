from flask import Blueprint, request, jsonify
from app.models.job import Job
from app.forms.job import JobForm # Importe o Model e o Formulário

job = Blueprint('job', __name__)

@job.route('/jobs', methods=['POST'])
def create_job():
    """Cria um novo job."""
    try:
        # Verifica se o conteúdo da solicitação é JSON
        if request.content_type == 'application/json':
            # Decodifica os dados JSON
            data = request.get_json()
            form = JobForm(data)
        else:
            form = JobForm(request.form)

        if form.is_valid():
            job = form.save()
            return jsonify({'status': 'success', 'job_id': job.id}), 201
        else:
            return jsonify({'status': 'error', 'errors': form.errors}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500