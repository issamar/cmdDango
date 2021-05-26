from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import sys
from .forms import LaboForm
from . models import Labo
from django.db.models import Sum
# Create your views here.

def calcLab(request):
	form = LaboForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			form = LaboForm()
	return render(request, 'calcLab.html', {'form' : form})


def vislab(request):
	get_data = Labo.objects.all().order_by('-dt')
	if request.method== 'POST':
		req = request.POST
		dep = req['sdate']
		fin = req['ldate']
		
		get_sdata = Labo.objects.filter(dt__lte = fin).filter(dt__gte=dep)
		return render(request, 'filterlab.html', {'getsdata' : get_sdata})
	context = {
		'getdata' : get_data
	}
	return render(request,'editlab.html',context)




def editPrev(request, pk):
	get_row = Labo.objects.get(id = pk)
	form = LaboForm(instance= get_row )
	if request.method == "POST":
		form  = LaboForm(request.POST, instance=get_row)
		if form.is_valid():
			form.save()
			return redirect('/lab/vislab/')
		
	context = {
		'form' : form
	}
	return render(request, 'editverlab.html', context)

def labStat(request):
	if request.method== 'POST':
		req = request.POST
		dep = req['startdt']
		fin = req['endt']
		count_stat_data = Labo.objects.filter(dt__lte = fin).filter(dt__gte=dep).count()
		pre_lab_stat_data = Labo.objects.filter(dt__lte = fin).filter(dt__gte=dep).aggregate(Sum('lab_price'))
		lab_stat_data = pre_lab_stat_data['lab_price__sum']
		pre_ph_stat_data = Labo.objects.filter(dt__lte = fin).filter(dt__gte=dep).aggregate(Sum('price'))
		ph_stat_data = pre_ph_stat_data['price__sum']
		return render(request, 'labstat.html', {'count' : count_stat_data, 'labprice' : lab_stat_data, 'price' : ph_stat_data})
	
	return render(request, 'labstat.html')
