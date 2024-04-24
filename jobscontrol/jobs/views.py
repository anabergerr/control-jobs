from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

def list_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/list_jobs.html', {'jobs': jobs})

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_jobs')
    else:
        form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': form})

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
