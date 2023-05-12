from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    # Define your fields here
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
