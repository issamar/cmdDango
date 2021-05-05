from django.shortcuts import render, redirect
from .forms import ClosureForm
from .models import Closure
# Create your views here.

def closure(request):
	form = ClosureForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'form' : form

	}
	return render(request,'cloture.html', context)


def showData(request):
	all_data = Closure.objects.all()
	context = {
		'datas' : all_data
	}
	return render(request,'visualiser.html', context)
