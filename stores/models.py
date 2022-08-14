from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length= 64)
    description = models.TextField( blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Post(models.Model):
    anything = models.CharField(max_length=256)

    def __str__(self):
        return self.anything