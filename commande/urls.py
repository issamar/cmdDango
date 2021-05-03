from django.urls import path
from commande.views import commandeAdd, addView, deleteView, addArtView, deleteArtView, markView, markViewArt

urlpatterns = [
	path('', commandeAdd, name='commande'),
	path('add/', addView, name='addcmd'),
	path('delete/<int:item_id>/', deleteView, name='deletecmd'),
	path('mark/<int:item_id>/', markView, name='markcmd'),

	path('addArt/', addArtView, name='addartcmd'),
	path('deleteart/<int:art_id>/', deleteArtView, name='deleteartcmd'),
	path('markart/<int:art_id>/', markViewArt, name='markartcmd'),
]