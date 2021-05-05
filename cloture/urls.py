from django.urls import path
from .views import closure, showData



urlpatterns = [
	path('', closure, name="cloture" ),
	path('visualiser/', showData, name="visualiser" ),
]