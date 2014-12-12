from django.db import models

class Video(models.Model):
  id = models.AutoField(primary_key=True)
  vidpath = models.FileField(upload_to='documents/%Y/%m/%d')

class Tag(models.Model):
  video = models.ForeignKey('Video')
  tagNum = models.IntegerField()
  x = models.IntegerField()
  y = models.IntegerField()
  r = models.FloatField()
  time = models.FloatField()

class Evaluation(models.Model):
  video = models.ForeignKey('Video')
  rep_num = models.IntegerField()
  evaluation = models.TextField()
