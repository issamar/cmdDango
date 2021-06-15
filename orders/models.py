from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Commande(models.Model):
	creation_date = models.DateField(auto_now_add=True)
	product = models.CharField(max_length=250)
	productype = models.CharField(max_length=100)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100)
	completed = models.BooleanField(default= False)
