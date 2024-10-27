from django.db import models
from django.contrib.auth.models import User

class Patients(models.Model):

    name = models.CharField(max_length=15,default='-')
    email = models.EmailField(max_length=20,default='-')
    gender = models.CharField(max_length=8,default='-')
    age = models.IntegerField(default='-')
    marital_status= models.CharField(max_length=10,default='-')   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Patients_mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=15,default='-')
    emotions = models.CharField(max_length=200,default='-')






