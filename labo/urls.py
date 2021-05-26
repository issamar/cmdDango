from django.urls import path, include
from labo.views import calcLab, vislab, editPrev, labStat

urlpatterns = [
	path('', calcLab, name="calclab" ),
	path('vislab/', vislab, name="vislab" ),
	path('editprev/<int:pk>', editPrev, name="editprev" ),
	path('labstat/', labStat, name="labstat" ),
	]