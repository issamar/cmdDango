from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user, allowed_users 
# Create your views here.
@unauthenticated_user
def registerPage(request):
	form = CreatUserForm()
	if request.method =='POST':
		form = CreatUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request," Account Created")
			return redirect('login')
	context = {
		'form' : form

	}
	return render(request,'register.html', context)


@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, "Username Or Password is incorrect")
	context = {

	
	}
	return render(request,'login.html', context)

def logoutPage(request):
	logout(request)
	return redirect("login")

@login_required(login_url='login')
def accueil(request):
	return render(request,"acceuil/accueil.html")
