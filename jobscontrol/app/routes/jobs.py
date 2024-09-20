from flask import Blueprint, request, jsonify
from app.models import db, Job

jobs_bp = Blueprint('jobs', __name__) 

@jobs_bp.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = db.session.query(Job).all()
    job_list = [job.as_dict() for job in jobs]
    return jsonify(job_list), 200

from flask import Blueprint, request, jsonify
from app.models import db, Job
from datetime import datetime

@jobs_bp.route('/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    # Converte a string de data para um objeto datetime
    date_obj = datetime.fromisoformat(data['date'])
    new_job = Job(
        name_job=data['name_job'],
        sequence_job=data['sequence_job'],
        name_company=data['name_company'],
        result_job=data['result_job'],
        obs_job=data.get('obs_job'),  # obs_job é opcional, então usamos get() para evitar erro se não for fornecido
        date=date_obj
    )
    db.session.add(new_job)
    db.session.commit()
    print(data)
    return jsonify({'message': 'Job created successfully!'}), 201
