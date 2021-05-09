from django.urls import path
from .views import closure, showData, visulizeToEdit, editAdForm, userEdition



urlpatterns = [
	path('', closure, name="cloture" ),
	path('visualiser/', showData, name="visualiser" ),
	path('viseforedit/', visulizeToEdit, name="visedit" ),
	path('editad/<int:pk>', editAdForm, name="editad" ),
	path('useredit/<int:pk>', userEdition, name="editus" ),
	]