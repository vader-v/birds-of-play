from django.db import models
from django.urls import reverse

class Bird(models.Model):
  name = models.CharField(max_length=200)
  origin = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  times_seen = models.IntegerField()
  
  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("bird-detail", kwargs={"bird-id": self.id})
  