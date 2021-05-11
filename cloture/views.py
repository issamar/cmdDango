from django.shortcuts import render, redirect
from .forms import ClosureForm, PartielClosureForm, BordereauxForm, EditBrdFrom
from .models import Closure, Bordereaux
from django.views.generic import UpdateView
import sys
from django.contrib.auth.decorators import login_required
from gestion_accueil.decorators import unauthenticated_user, allowed_users
import datetime
# Create your views here.
@login_required(login_url='login')
def closure(request):
	form = ClosureForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ClosureForm()
	context = {
		'form' : form

	}
	return render(request,'cloture.html', context)

@login_required(login_url='login')
def showData(request):
	some_data = Closure.objects.all().order_by('-id')[:10]
	context = {
		'datas' : some_data
	}
	return render(request,'visualiser.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def visulizeToEdit(request):
	get_data = Closure.objects.all().order_by('-id')
	context = {
		'getdata' : get_data
	}
	return render(request,'visedit.html',context)


@login_required(login_url='login')
def editAdForm(request, pk):
	row = Closure.objects.get(id=pk)
	form = ClosureForm(instance=row)
	if request.method == "POST":
		form  = ClosureForm(request.POST, instance=row)
		
		if form.is_valid():
			print(form.cleaned_data)
			sys.stdout.flush()
			#get data one by one from the form before saving it
			cleaned_form = form.cleaned_data
			wasfa_amount = cleaned_form['wasfa']
			str_money = cleaned_form['start_money']
			clo_money = cleaned_form['closure_money']
			clo_paper = cleaned_form['closure_paper']
			ecart_money = cleaned_form['money']
			getdetail = cleaned_form['details']
			#calculate the real maney + Ecart
			real_mny = (clo_paper + clo_money) - str_money
			get_real_money = Closure.objects.get(id=pk)
			get_real_money.real_money= real_mny
			ecart_calc = (real_mny - wasfa_amount ) - ecart_money 
			#save edited data
			get_real_money.ecart = ecart_calc
			get_real_money.money = ecart_money
			get_real_money.details = getdetail
			get_real_money.wasfa = wasfa_amount
			form.save()
			get_real_money.save()

			return redirect('/cloture/viseforedit')
	context = {
		'form' : form
	}
	return render(request,'editad.html', context)

@login_required(login_url='login')
def userEdition(request, pk):
	idid = Closure.objects.get(id=pk)
	form = PartielClosureForm(instance=idid)
	if request.method == 'POST':
		form  = PartielClosureForm(request.POST, instance=idid)

		if form.is_valid():
			washed_form = form.cleaned_data
			print(washed_form)
			sys.stdout.flush()
			form.save()
			return redirect('/cloture/visualiser/')

	context = {
		'form' : form
	}
	return render(request,'useredit.html', context)


	# suivi des borderaux views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def convention(request):
	all_brd = Bordereaux.objects.all()
	form = BordereauxForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		form = BordereauxForm()
	context = {
		'form' : form, 'brds' : all_brd
		}
	return render(request,'brd.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def editBrd(request, pk):
	get_id = Bordereaux.objects.get(id=pk)
	form = EditBrdFrom(instance=get_id)
	if request.method == 'POST':
		form = EditBrdFrom(request.POST, instance=get_id)
		if form.is_valid():
			pure_data = form.cleaned_data
			get_data = Bordereaux.objects.get(id=pk)
			#get the date of payement
			dtjrl = str(pure_data['dt_jrl'])
			date1 = datetime.datetime.strptime(dtjrl, "%Y-%m-%d")
			datep = date1 + datetime.timedelta(days=15)
			get_data.dt_pay = datep
			#get the ord def
			nordj = pure_data['n_ord_jrl']
			nord = pure_data['n_ord']
			ord_ = nord - nordj
			get_data.def_o = ord_
			#get the amount def
			m_j = pure_data['m_jrl']
			m_b = pure_data['m_brd']
			defr = m_b - m_j
			get_data.defr= defr
			get_data.save()
			form.save()
			return redirect('/cloture/sbrd/')

	context = {
		'form' : form
	}
	return render(request, 'editbrd.html', context)