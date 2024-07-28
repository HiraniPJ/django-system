from django.db import models
from django.contrin.auth.models import User


# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=150)
    details=models.TextField()

