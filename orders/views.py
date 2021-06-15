from django.shortcuts import render, redirect
from .forms import CmdForm
from .models import Commande
import sys
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def easyCmd(request):
	get_mdc = Commande.objects.filter(productype='Médicament').order_by('creation_date')
	get_art = Commande.objects.filter(productype='Article').order_by('creation_date')
	get_other = Commande.objects.filter(productype='Autres').order_by('creation_date')
	form = CmdForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			get_prod_name = Commande.objects.values_list('product', flat=True)
			current_product = request.POST['product']
			print(current_product.upper())
			sys.stdout.flush()
			if current_product.lower() not in get_prod_name:
				form.save()
				form = CmdForm()
			else:
			 	messages.error(request,'Ce Produit exist deja ')
			 	form = CmdForm()
	context = {
	'mdcs' : get_mdc,'form' : form, 'arts': get_art,'autres' : get_other
	}
	return render(request,'index.html',context)

@login_required(login_url='login')
def manageItems(request):
	if 'cmd' in request.POST:
		checked_items = request.POST.getlist('checks')
		for item in checked_items:
			get_seleted_db = Commande.objects.get(product=item)
			get_seleted_db.completed = True
			get_seleted_db.save()
	if 'arr' in request.POST:
		checked_items = request.POST.getlist('checks')
		for item in checked_items:
			get_seleted_db = Commande.objects.get(product=item)
			get_seleted_db.delete()
	return HttpResponseRedirect('/orders')




def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else : 
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else : 
				messages.info(request, "Nom d'utilisateur ou Mot de passe est incorrect")


		return render(request,'login.html', {})

def logoutUser(request):
	logout(request)
	return redirect('login')