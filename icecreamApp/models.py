from datetime import date
import email
from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    Phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
