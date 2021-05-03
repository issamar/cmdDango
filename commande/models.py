from django.db import models

# Create your models here.

class Cmd(models.Model):
	name = models.CharField(max_length=250)
	med_cmded = models.BooleanField(default=False)

class CmdArt(models.Model):
	nameart = models.CharField(max_length=350)
	art_cmded = models.BooleanField(default=False) 
