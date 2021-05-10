from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Closure(models.Model):
	creation_date = models.DateTimeField(auto_now_add=True)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	start_money = models.IntegerField()
	closure_money = models.IntegerField()
	closure_paper = models.IntegerField()
	money = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True, default=0)
	details = models.CharField(max_length=200, blank=True, null=True)
	wasfa = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True, default=0)
	real_money = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
	ecart = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)


class Bordereaux(models.Model):
	pay_ctr = models.CharField(max_length=20)
	n_brd = models.IntegerField(unique=True)
	dt_clo = models.DateField()
	n_ord = models.IntegerField()
	m_brd = models.DecimalField(decimal_places=2, max_digits=8)
	dt_depot = models.DateField(null=True, blank=True)
	dt_jrl = models.DateField(null=True, blank=True)
	n_ord_jrl = models.IntegerField( null=True, blank=True)
	m_jrl = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
	dt_pay = models.DateField( null=True, blank=True)
	defr = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
	payement = models.BooleanField(default=False)