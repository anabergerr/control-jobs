from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_jobs, name='list_jobs'),
    path('jobs/', views.list_jobs, name='list_jobs'),
    path('create/', views.create_job, name='create_job'),
    path('update/<int:id>/', views.update_job, name='update_job'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
]
