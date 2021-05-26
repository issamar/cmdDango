from django.db import models

# Create your models here.


class Labo(models.Model):
	dt = models.DateField(auto_now_add = True)
	p_name = models.CharField(max_length = 200)
	dob = models.DateField()
	params = models.TextField(max_length=500)
	lab_price = models.IntegerField(default = 0)
	price = models.IntegerField(default = 0)
	pay = models.IntegerField(default = 0)
	rest = models.IntegerField(default=0)
	info = models.TextField(max_length=200, blank = True)