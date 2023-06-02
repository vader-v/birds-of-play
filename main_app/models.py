from django.db import models

class Bird(models.Model):
  name = models.CharField(max_length=200)
  origin = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  times_seen = models.IntegerField()
  
  def __str__(self):
      return self.name