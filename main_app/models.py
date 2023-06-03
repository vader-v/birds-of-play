from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Bird(models.Model):
  name = models.CharField(max_length=200)
  origin = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  times_seen = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("bird-detail", kwargs={"bird-id": self.id})
  