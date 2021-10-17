from django.db import models

# Create your models here.


class Companies(models.Model):
    roll_no = models.CharField(max_length=10)
    s_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=50)
