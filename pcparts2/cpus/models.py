from django.db import models

class CPUS(models.Model):
  cpuman = models.CharField(max_length=255)
  cpuname = models.CharField(max_length=255)
  cpusocket = models.CharField(max_length=255)
  cpucores = models.CharField(max_length=255)
  cputhreads = models.CharField(max_length=255)
