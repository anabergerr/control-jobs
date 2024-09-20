from flask import Blueprint, request, jsonify
from app.models import db, Job

bp = Blueprint('get', __name__)

@bp.get('/jobs')
def get_jobs():
    jobs = db.session.query(Job).all()
    job_list = [job.as_dict() for job in jobs]
    return jsonify(job_list), 200
