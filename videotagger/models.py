from django.db import models

class AnnoVideo(models.Model):
  vidpath = models.FileField(upload_to='documents/%Y/%m/%d')
