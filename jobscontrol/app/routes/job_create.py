from flask import Blueprint, request, jsonify
from app.models import db, Job
from datetime import datetime

bp = Blueprint('routes', __name__)

@bp.route('/create', methods=['POST'])
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
