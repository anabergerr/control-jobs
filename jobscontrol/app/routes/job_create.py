from flask import Blueprint, request, jsonify
from app.models import db, Job
from datetime import datetime

bp = Blueprint('routes', __name__)

@bp.route('/create', methods=['POST'])
def create_job():
    data = request.get_json()
    # Converte a string de data para um objeto datetime
    date_obj = datetime.fromisoformat(data['date'])
    new_job = Job(name=data['name'], date=date_obj)
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job created successfully!'}), 201
