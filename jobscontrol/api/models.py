from django.db import models

from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=100)
    type_job = models.CharField(max_length=50)
    YES = 'Yes'
    NO = 'No'
    COMPANY_RETURN_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    company_return = models.CharField(
        max_length=3,
        choices=COMPANY_RETURN_CHOICES,
        default=NO,
    )
    date = models.DateField(default=timezone.now)

