from django.shortcuts import render, redirect,get_object_or_404
from .models import Job
from .forms import JobForm
from django.http import JsonResponse
from django.http import JsonResponse
import json

def list_jobs(request):
    jobs = Job.objects.all()
    job_list = [{'id': job.id, 'title': job.title, 'type_job': job.type_job, 'company_return': job.company_return, 'date': job.date} for job in jobs]
    return JsonResponse(job_list, safe=False)

def create_job(request):
    try:
        # Verifica se o conteúdo da solicitação é JSON
        if request.content_type == 'application/json':
            # Decodifica os dados JSON
            data = json.loads(request.body)
            form = JobForm(data)
        else:
            form = JobForm(request.POST)

        if form.is_valid():
            job = form.save()
            return JsonResponse({'status': 'success', 'job_id': job.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)



def update_job(request, id):
    try:
        job = Job.objects.get(id=id)
        if request.method == 'POST':
            # Se for uma solicitação POST, atualize o job com os dados fornecidos
            data = json.loads(request.body)
            form = JobForm(data, instance=job)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'success', 'message': 'Job atualizado com sucesso'})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        else:
            # Se for uma solicitação GET, retorne os dados do job como JSON
            job_data = {'title': job.title, 'type_job': job.type_job, 'company_return': job.company_return, 'date': job.date}  
            return JsonResponse({'status': 'success', 'job': job_data})
    except Job.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Job não encontrado'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)



def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    
    if request.method == 'DELETE':
        job.delete()
        return JsonResponse({'message': 'Job deleted successfully'})
    
    return JsonResponse({'error': 'DELETE request required'}, status=400)


