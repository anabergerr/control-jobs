from django.db import models

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    type_job = models.CharField(max_length=50)
    company_return = models.TextField()

