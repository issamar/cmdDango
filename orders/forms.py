from django import forms
from .models import Commande



class CmdForm(forms.ModelForm):
	class Meta:
		model = Commande
		fields = ['product','productype','tags','username']
		CTR_CHOICES = (
			('', ''),
			('Médicament','Médicament'),
			('Article','Article'),
			('Autres','Autres'))

		TAG_CHOICES = (
			('',''),
			('Rupture','Rupture'),
			('Faible','Faible'),
			('Ord','Ord')
			)
		labels = {
			'product':('Nom de produit'),
			'productype' : ('Le type de produit'),
			'tags' : ('Tager le produit'),
			'username' : ('Le Nom d\'utilisateur')
		}
		widgets = {
			'product': forms.TextInput(attrs={
			'id' : 'product',
			'class' : 'form-control ',
			'placeholder': 'Nom de Produit',
			'autofocus': 'True'

			}),
			'productype' : forms.Select(choices= CTR_CHOICES, attrs = {
				'id' : 'type',
				'class' : 'form-control ',
				'placeholder': 'Type De Produit'
				}),
			'tags' : forms.Select(choices= TAG_CHOICES, attrs={
				'id' : 'tag',
				'class' : 'form-control ',
				'placeholder': 'Tag de Produit'
				}),
			'username' : forms.Select(attrs = {
				'id' : 'user',
				'class' : 'form-control ',
				'placeholder': "Nom d'Utilisateur"
				})
		}