from django.urls import path
from .views import closure, showData, visulizeToEdit, editAdForm, userEdition, convention, editBrd,addBrdView, stat, cashstat


urlpatterns = [
	path('', closure, name="cloture" ),
	path('visualiser/', showData, name="visualiser" ),
	path('viseforedit/', visulizeToEdit, name="visedit" ),
	path('editad/<int:pk>', editAdForm, name="editad" ),
	path('useredit/<int:pk>', userEdition, name="editus" ),
	path('sbrd/', convention, name='convention'),
	path('editbrd/<int:pk>', editBrd, name='editbrd'),
	path('sbrd/add/', addBrdView, name='addbrd'),
	path('stat/', stat, name='stat'),
	path('cashstat/', cashstat, name='cashstat'),

	]