from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_restx import Api, Resource, fields
from api.models import Job
from api.schemas import job_schema
from flask import request
from app import db

# def list_jobs(request):
#     jobs = Job.objects.all()
#     job_list = [{'id': job.id, 'title': job.title, 'type_job': job.type_job, 'company_return': job.company_return, 'date': job.date} for job in jobs]
#     return JsonResponse(job_list, safe=False)



app = Flask(__name__)

api = Api(app)

class JobResource(Resource):
    @api.expect(job_schema)  # Adicione validate=True para validar os dados
    @api.marshal_with(job_schema, code=201, description='Job criado com sucesso')
    def post(self):
        """Cria um novo Job."""
        data = request.get_json()
        print('DATA', data)
        try:
            # Validar os dados usando o schema (indiretamente):
            # A validação é feita pelo @api.expect(job_schema, validate=True)
            
            # Criar o Job
            job = Job(title=data['title'], type_job=data['type_job'], date=data['date']) 
            db.session.add(job)
            db.session.commit()

            # Serializar e retornar o Job criado:
            return job, 201 

        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 500


# def update_job(request, id):
#     job = Job.objects.get(id=id)
#     if request.method == 'POST':
#         form = JobForm(request.POST, instance=job)
#         if form.is_valid():
#             form.save()
#             return redirect('list_jobs')
#     else:
#         form = JobForm(instance=job)
#     return render(request, 'jobs/update_job.html', {'form': form})

# def delete_job(request, id):
#     job = get_object_or_404(Job, id=id)
    
#     if request.method == 'DELETE':
#         job.delete()
#         return JsonResponse({'message': 'Job deleted successfully'})
    
#     return JsonResponse({'error': 'DELETE request required'}, status=400)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)