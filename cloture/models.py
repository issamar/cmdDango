from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Closure(models.Model):
	creation_date = models.DateTimeField(auto_now_add=True)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	start_money = models.IntegerField()
	closure_money = models.IntegerField()
	closure_paper = models.IntegerField()
	money = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
	details = models.CharField(max_length=200, blank=True, null=True)
	wasfa = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
	real_money = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
	ecart = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
