from django.db import models

class Task(models.Model):
  taskname = models.CharField(max_length=255)
  deadline = models.CharField(max_length=255)
