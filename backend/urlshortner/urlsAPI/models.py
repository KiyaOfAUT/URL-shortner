from django.db import models

# Create your models here.


class urls(models.Model):
    shortURL = models.CharField(max_length=50, primary_key=True)
    mainURL = models.CharField(max_length=500)
