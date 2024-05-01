from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
from django.http import JsonResponse



def list_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/list_jobs.html', {'jobs': jobs})


def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            # Você pode retornar os dados do job criado como JSON, se necessário
            return JsonResponse({'status': 'success', 'job_id': job.id})
        else:
            # Se o formulário não for válido, você pode retornar os erros como JSON
            print(form.errors)
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        # Se o método da requisição não for POST, você pode retornar um erro adequado
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


def update_job(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('list_jobs')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/update_job.html', {'form': form})

def delete_job(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        job.delete()
        return redirect('list_jobs')
    return render(request, 'jobs/delete_job.html', {'job': job})


