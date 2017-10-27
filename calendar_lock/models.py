from django.db import models

# Create your models here.
from django.db.models.fields import DateField, CharField


class Date_lock(models.Model):
    date_locked=DateField(unique=True)
    reason_locked=CharField(max_length=200,default="Sin motivo")

