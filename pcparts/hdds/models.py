from django.db import models

class hdd(models.Model):
  hddname = models.CharField(max_length=255)
  hddstatus = models.CharField(max_length=255)
  hddmemory=models.IntegerField(default = 0)
  hddyear=models.IntegerField(default = 2000)
  hdddate=models.DateField(auto_now=True)
