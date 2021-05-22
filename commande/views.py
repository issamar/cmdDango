from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cmd, CmdArt
import sys
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def commandeAdd(request): # function to display medocs and articles
	all_cmd = Cmd.objects.all().order_by('name')
	all_cmd_art = CmdArt.objects.all().order_by('nameart')
	
	
	context = {
		'medocs' : all_cmd, 'arts' : all_cmd_art
	}
	return render(request, 'commande.html', context)

@login_required(login_url='login')
def addView(request): # function to add medoc to the database
	all_cmd_names = Cmd.objects.values_list('name', flat=True)
	mdc = Cmd(name=request.POST['name'])
	mdc_name = mdc.name
	if mdc_name not in all_cmd_names:
		mdc.save()
	else:
		messages.error (request, 'Ce Medicament/Article Existe Deja')
	context = {
		'mdc' : mdc
	}
	return HttpResponseRedirect('/commande')

@login_required(login_url='login')
def markView(request, item_id): # function to mark commanded medocs
	mark_id = Cmd.objects.get(id=item_id)
	mark_id.med_cmded = True 
	mark_id.save()

	return HttpResponseRedirect('/commande')


@login_required(login_url='login')

def deleteView(request, item_id): # function to delete medoc from db
	itemToDelete = Cmd.objects.get(id=item_id)
	itemToDelete.delete()
	return HttpResponseRedirect('/commande')

@login_required(login_url='login')
def addArtView(request): # function to add artcles to the database
	all_cmd_names_art = CmdArt.objects.values_list('nameart', flat=True)
	art = CmdArt(nameart=request.POST['nameart'])
	art_name = art.nameart
	if art_name not in all_cmd_names_art:
		art.save()
	else:
		messages.error (request, 'Ce Medicament/Article Existe Deja', extra_tags='art')
	# art = CmdArt(nameart=request.POST['nameart'])
	# if art.is_valid():
	# 	art.save()
	context = {
		'art' : art
	}
	return HttpResponseRedirect('/commande')

@login_required(login_url='login')
def deleteArtView(request, art_id): # a function to remove articles from database
	artToDelete = CmdArt.objects.get(id=art_id)
	artToDelete.delete()
	return HttpResponseRedirect('/commande')

@login_required(login_url='login')
def markViewArt(request, art_id): #function to mark commanded articls
	mark_id_art = CmdArt.objects.get(id=art_id)
	mark_id_art.art_cmded = True 
	mark_id_art.save()

	return HttpResponseRedirect('/commande')