from flask import Blueprint, request, jsonify
from app.models import db, Job
from datetime import datetime
import logging

jobs_bp = Blueprint('jobs', __name__) 

@jobs_bp.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = db.session.query(Job).all()
    job_list = [job.as_dict() for job in jobs]
    return jsonify(job_list), 200

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

<<<<<<< HEAD
@jobs_bp.route('/jobs', methods=['DELETE'])
def delete_job():
    data = request.get_json()

    if 'id_job' not in data:
        return jsonify({'error': 'Job ID not provided.'}), 400
   
    id_job = data['id_job']
    job = Job.query.get(id_job)

    if job is None:
        return jsonify({'error': 'Job not found.'}), 404

    try:
        db.session.delete(job)
        db.session.commit()
        return jsonify({'message': 'Job deleted successfully.'}), 200
    except Exception as e:
        if isinstance(e, db.exc.IntegrityError):
            return jsonify({'error': 'Database integrity error while deleting job.'}), 500
        else:
            logging.exception(str(e))
            return jsonify({'error': 'An error occurred while deleting the job.'}), 500
    
=======

@jobs_bp.route('/jobs/<int:id>', methods=['PATCH'])
def update_job_partial(id):
    data = request.get_json()
    job = Job.query.get(id)
    
    if not job:
        return jsonify({'message': 'Job not found'}), 404

    # Campos permitidos para atualização
    allowed_fields = ['name_job', 'sequence_job', 'name_company', 'result_job', 'obs_job', 'date']

    # Itera sobre os campos recebidos e atualiza o job
    for field in data:
        if field in allowed_fields:
            if field == 'date':  # Converte a data se for o campo 'date'
                setattr(job, field, datetime.fromisoformat(data[field]))
            else:
                setattr(job, field, data[field])

    db.session.commit()
    return jsonify({'message': 'Job updated partially!'}), 200
>>>>>>> 17eccb677f22ccf9d5d42568b63f2226e9a39f6c
