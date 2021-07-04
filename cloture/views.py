from django.shortcuts import render, redirect
from .forms import ClosureForm, PartielClosureForm, BordereauxForm, EditBrdFrom
from .models import Closure, Bordereaux
from django.views.generic import UpdateView
import sys
from django.contrib.auth.decorators import login_required
from gestion_accueil.decorators import unauthenticated_user, allowed_users
import datetime
from django.contrib import messages
from django.db.models import Sum, Avg, Min, Max, Count
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import make_aware
from django.db.models.functions import TruncDay
# Create your views here.


@login_required(login_url='login')
def closure(request):
	user_name = request.user
	some_data = Closure.objects.all().order_by('-id')[:12]
	
	form = ClosureForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.username = user_name
		str_money = instance.start_money
		clt_money = instance.closure_money
		clt_paper = instance.closure_paper
		real_money = (clt_paper + clt_money) - str_money
		instance.real_money = real_money
		instance.save()
		form = ClosureForm()
	context = {
		'form' : form, 'datas' : some_data

	}
	return render(request,'cloture.html', context)

@login_required(login_url='login')
def showData(request):

	return redirect('cloture')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def visulizeToEdit(request):
	get_data = Closure.objects.all().order_by('-id')[:60]
	context = {
		'getdata' : get_data
	}
	return render(request,'visedit.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def cashstat(request):
	users = User.objects.all()
	get_data = Closure.objects.values(day=TruncDay('creation_date')).annotate(Sum('closure_paper'), Sum('wasfa'), Sum('real_money'), Sum('ecart')).order_by('-day')
	count = Closure.objects.values(day=TruncDay('creation_date')).annotate(Count('creation_date')).count()
	pre_get_sum = Closure.objects.all().aggregate(Sum('closure_paper'))
	get_sum = round(pre_get_sum['closure_paper__sum'],2)
	calc_avg = get_sum / count
	get_mincash = Closure.objects.values(day=TruncDay('creation_date')).annotate(Sum('closure_paper')).values_list('closure_paper__sum', flat=True)
	mincash=min(get_mincash)
	get_maxcash = Closure.objects.values(day=TruncDay('creation_date')).annotate(Sum('closure_paper')).values_list('closure_paper__sum', flat=True)
	maxcash=max(get_maxcash)
	get_all_gap = Closure.objects.all().aggregate(Sum('ecart'))
	all_gap = round(get_all_gap['ecart__sum'],2)
	if request.method == 'POST':
		data =  request.POST
		usern= data['usern']
		aware_sdate= make_aware(datetime.datetime.strptime(data['sdate'], '%Y-%m-%d'))
		edate = make_aware(datetime.datetime.strptime(data['edate'], '%Y-%m-%d'))
		aware_edate = edate + datetime.timedelta(days=1)

		#count = Closure.objects.values(day=TruncDay('creation_date')).annotate(Count('creation_date')).count()
		count = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).values(day=TruncDay('creation_date')).annotate(Count('creation_date')).count()
		if count == 0:
			messages.error(request,' You have no Data in This Range Of Time ')
			return render(request,'cashstat.html', {'datas' : get_data,'users' : users})
		if count != 0:
			if usern == "":
				pre_cash = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).aggregate(total=Sum('closure_paper'))
				cash = pre_cash['total']
				avg = round((cash / count),2)
				get_cash = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).values(day=TruncDay('creation_date')).annotate(Sum('closure_paper')).values_list('closure_paper__sum', flat=True)
				min_cash=min(get_cash)
				max_cash = max(get_cash)
				pre_get_gap = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).aggregate(Sum('ecart'))
				get_gap=round(pre_get_gap['ecart__sum'])
				get_data = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).values(day=TruncDay('creation_date')).annotate(Sum('closure_paper'), Sum('wasfa'), Sum('real_money'), Sum('ecart')).order_by('-day')
				return render(request,'cashstat.html',{'count' : count, 'cash' : cash, 'avg': avg, 
					'mincash' : min_cash,'maxcash':max_cash,'gap':get_gap, 'datas': get_data,
					'users' : users})
			if usern != "" :
				count = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).filter(username__username= usern).count()
				pre_cash = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).filter(username__username = usern).aggregate(Sum('closure_paper'))
				cash = pre_cash['closure_paper__sum']
				avg = round((cash/count),2)
				get_cash = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).filter(username__username= usern).values_list('closure_paper', flat=True)
				min_cash = min(get_cash)
				max_cash = max(get_cash)
				pre_get_gap = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).filter(username__username=usern).aggregate(Sum('ecart'))
				get_gap = round(pre_get_gap['ecart__sum'])
				get_data = Closure.objects.filter(creation_date__gte=aware_sdate).filter(creation_date__lte=aware_edate).filter(username__username=usern).order_by('-creation_date')
				return render(request, 'cashstat.html', {'users' : users, 'cash' : cash, 'count' : count,
					'avg': avg,'mincash' : min_cash,'maxcash':max_cash,'gap':get_gap, 'sdata': get_data})
	return render(request,'cashstat.html', {'datas' : get_data,'users' : users, 'count' :  count,
				 'cash' : get_sum, 'avg' : calc_avg, 'mincash': mincash, 'maxcash' : maxcash, 'gap' : all_gap})







@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def editAdForm(request, pk):
	row = Closure.objects.get(id=pk)
	form = ClosureForm(instance=row)
	if request.method == "POST":
		form  = ClosureForm(request.POST, instance=row)
		
		if form.is_valid():
			inst = form.save(commit=False)
			get_gap = inst.money
			get_soft = inst.wasfa
			get_real_money = Closure.objects.get(id=pk).real_money
			gap = (get_real_money - get_soft) - get_gap
			inst.ecart = gap
			form.save()

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
			ecart_money = washed_form['money']
			r_money = Closure.objects.get(id=pk).real_money
			w_money = Closure.objects.get(id=pk).wasfa
			ecart_calc = (r_money - w_money ) - ecart_money
			idid.ecart = ecart_calc 
			form.save()
			idid.save()
		return redirect('/cloture/visualiser/')

	context = {
		'form' : form
	}
	return render(request,'useredit.html', context)





	# suivi des borderaux views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def convention(request):
	all_brd = Bordereaux.objects.all().order_by('dt_clo')
	# form = BordereauxForm(request.POST or None)
	# if request.method == 'POST':
	# 	form = BordereauxForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		messages.success(request,'Bordereau Ajouter Avec Succés')
	form = BordereauxForm()
	context = {
		'form' : form, 'brds' : all_brd}
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
			ord_ = nordj - nord
			get_data.def_o = ord_

			#get the amount def
			m_j = pure_data['m_jrl']
			m_b = pure_data['m_brd']
			defr = m_j - m_b
			get_data.defr= defr
			get_data.dt_jrl=dtjrl
			get_data.n_ord_jrl = nordj
			get_data.m_jrl= m_j
			#pay status
			pay_stat = pure_data['payement']
			get_data.payement = pay_stat
			
			form.save()
			get_data.save()
			
			return redirect('/cloture/sbrd/')

	context = {
		'form' : form
	}
	return render(request, 'editbrd.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addBrdView(request):
	form = BordereauxForm(request.POST or None)
	if request.method == 'POST':
		form = BordereauxForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Bordereau Ajouter Avec Succés')
		
	context = {

		'form' : form
	}
	return HttpResponseRedirect('/cloture/sbrd')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def stat(request):

	m_t_brd = Bordereaux.objects.aggregate(somme = Sum('m_brd'))
	mtbrd = round(m_t_brd['somme'],2)
	get_cnas = Bordereaux.objects.filter(pay_ctr = "CNAS").aggregate(sumcnas = Sum('m_brd'))
	cnas_t = round(get_cnas['sumcnas'],2)
	get_casnos = Bordereaux.objects.filter(pay_ctr = "CASNOS").aggregate(sumcasnos = Sum('m_brd'))
	casnos_t = round(get_casnos['sumcasnos'],2)
	get_cm = Bordereaux.objects.filter(pay_ctr = "Caisse Militaire").aggregate(sumcm = Sum('m_brd'))
	if get_cm['sumcm'] != None :
		cm_t = round(get_cm['sumcm'],2)
	else :
		cm_t = 0
	get_ecart = Bordereaux.objects.aggregate(sumecart=Sum('defr'))
	ecart_t = round(get_ecart['sumecart'],2)
	cnas_b = 0
	casnos_b = 0
	c_m_b = 0
	cnas_jrl=0
	casnos_jrl = 0
	c_m_jrl = 0
	cnas_e = 0
	casnos_e = 0
	c_m_e = 0
	if request.method == 'POST':
		req = request.POST
		dep = req['depart']
		# correct fin with adding one day
		fin = req['fin']
		# get the sum of each brd
		pre_cnas = Bordereaux.objects.filter(dt_clo__lte = fin).filter(dt_clo__gte=dep).filter(pay_ctr='CNAS').aggregate(sumbrd=Sum('m_brd'))
		pre_casnos = Bordereaux.objects.filter(dt_clo__lte = fin).filter(dt_clo__gte=dep).filter(pay_ctr='CASNOS').aggregate(sumbrd=Sum('m_brd'))
		pre_c_m = Bordereaux.objects.filter(dt_clo__lte = fin).filter(dt_clo__gte=dep).filter(pay_ctr='Caisse Militaire').aggregate(sumbrd=Sum('m_brd'))
		#get the sum of jrl
		pre_cnas_jrl = Bordereaux.objects.filter(dt_jrl__lte = fin).filter(dt_jrl__gte=dep).filter(pay_ctr='CNAS').aggregate(sumbrd=Sum('m_jrl'))

		pre_casnos_jrl = Bordereaux.objects.filter(dt_jrl__lte = fin).filter(dt_jrl__gte=dep).filter(pay_ctr='CASNOS').aggregate(sumbrd=Sum('m_jrl'))
		pre_c_m_jrl = Bordereaux.objects.filter(dt_jrl__lte = fin).filter(dt_jrl__gte=dep).filter(pay_ctr='Caisse Militaire').aggregate(sumbrd=Sum('m_jrl'))
		# get the sum of loss
		pre_cnas_e = Bordereaux.objects.filter(dt_clo__lte = fin).filter(dt_clo__gte=dep).filter(pay_ctr='CNAS').aggregate(sumbrd=Sum('defr'))
		pre_casnos_e = Bordereaux.objects.filter(dt_clo__lte = fin).filter(dt_clo__gte=dep).filter(pay_ctr='CASNOS').aggregate(sumbrd=Sum('defr'))
		
		pre_c_m_e = Bordereaux.objects.filter(dt_clo__lte = fin).filter(dt_clo__gte=dep).filter(pay_ctr='Caisse Militaire').aggregate(sumbrd=Sum('defr'))
		#try:
		if pre_cnas['sumbrd'] != None :
			cnas_b = round(pre_cnas['sumbrd'],2)
			
		else:
			cnas_b = 0
		if pre_casnos['sumbrd'] != None:
			casnos_b = round(pre_casnos['sumbrd'],2)
		else:
			casnos_b = 0
		if pre_c_m['sumbrd']!= None:
			c_m_b = round(pre_c_m['sumbrd'],2)
		else : 
			c_m_b = 0
		if pre_cnas_jrl['sumbrd'] != None:
			cnas_jrl = round(pre_cnas_jrl['sumbrd'])
		else:
			cnas_jrl = 0
		if pre_casnos_jrl['sumbrd'] != None:
			casnos_jrl = round(pre_casnos_jrl['sumbrd'],2)
		else:
			casnos_jrl = 0
		if pre_c_m_jrl['sumbrd']!= None:
			c_m_jrl = round(pre_c_m_jrl['sumbrd'],2)
		else :
			c_m_jrl = 0
		if pre_cnas_e['sumbrd'] != None:
			cnas_e = round(pre_cnas_e['sumbrd'],2)
		else:
			cnas_e = 0
		if pre_casnos_e['sumbrd'] != None:
			casnos_e = round(pre_casnos_e['sumbrd'],2)
		else:
			casnos_e = 0
		if pre_c_m_e['sumbrd'] != None:
			c_m_e = round(pre_c_m_e['sumbrd'],2)
		else : 
			c_m_e = 0
		m_t_brd = Bordereaux.objects.aggregate(somme = Sum('m_brd'))
		mtbrd = round(m_t_brd['somme'],2)
		get_cnas = Bordereaux.objects.filter(pay_ctr = "CNAS").aggregate(sumcnas = Sum('m_brd'))
		cnas_t = round(get_cnas['sumcnas'],2)
		get_casnos = Bordereaux.objects.filter(pay_ctr = "CASNOS").aggregate(sumcasnos = Sum('m_brd'))
		casnos_t = round(get_casnos['sumcasnos'],2)
		get_cm = Bordereaux.objects.filter(pay_ctr = "Caisse Militaire").aggregate(sumcm = Sum('m_brd'))
		if get_cm['sumcm'] != None :
			cm_t = round(get_cm['sumcm'],2)
		else :
			cm_t = 0
		get_ecart = Bordereaux.objects.aggregate(sumecart=Sum('defr'))
		ecart_t = round(get_ecart['sumecart'],2)

		return render(request,'stat.html', {
				'cnasb' : cnas_b, 'casnosb' : casnos_b, 'cmb' : c_m_b, 'cnasj' : cnas_jrl, 'casnosj' : casnos_jrl,
				'cmj' : c_m_jrl, 'cnase' : cnas_e, 'casnose' : casnos_e,'cme' : c_m_e,'mtbrd' : mtbrd, 'cnast' : cnas_t,
		'casnost': casnos_t, 'cm' : cm_t, 'ecartt' : ecart_t
				})
	context = {
		'mtbrd' : mtbrd, 'cnast' : cnas_t,
		'casnost': casnos_t, 'cm' : cm_t, 'ecartt' : ecart_t
	}
	return render(request,'stat.html', context)


