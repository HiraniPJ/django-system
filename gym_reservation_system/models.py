from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()

