from django.db import models

class cpu(models.Model):
  cpusname = models.CharField(max_length=255)
  cpusstatus = models.CharField(max_length=255)
  cpusmemory=models.IntegerField(default = 0)
  cpusyear=models.IntegerField(default = 2000)
  cpusdate=models.DateField(auto_now=True)
