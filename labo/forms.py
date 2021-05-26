from .models import Labo
from django import forms


class LaboForm(forms.ModelForm):
	class Meta:
		model = Labo
		fields = '__all__'

		labels = {
			'dt' : ('Date de Prelevement '),
			'p_name' : ('Nom et Prenom '),
			'dob' : ('Date de Naissance '),
			'params' : ('Les parametre faits'),
			'lab_price' : (''),
			'price' : ('Total '),
			'pay' : ('Versement'),
			'rest' : ('Le Reste '),
			'info' : ('Information Supplementaire ')
		}
		widgets = {
			'dt' : forms.DateInput(attrs = {
				'id' : 'dt_p',
				'class' : 'form-control',
				'type' : 'date'
				}),
			'p_name' : forms.TextInput(attrs = {
				'id' : 'pname',
				'class' : 'form-control',
				}),
			'dob' : forms.DateInput(attrs = {
				'id' : 'dob',
				'class' : 'form-control',
				'type' : 'date'
				}),
			'params' : forms.TextInput(attrs = {
				'id' : 'params',
				'class' : 'form-control',
				}),
			'lab_price' : forms.NumberInput(attrs = {
				'id' : 'lprice',
				'class' : 'form-control',
				}),
			'price' : forms.NumberInput(attrs = {
				'id' : 'price',
				'class' : 'form-control',
				}),
			'pay' : forms.NumberInput(attrs = {
				'id' : 'pay',
				'class' : 'form-control',
				'oninput' : 'reste()'
				}),
			'rest' : forms.NumberInput(attrs = {
				'id' : 'rest',
				'class' : 'form-control',

				}),
			'info' : forms.TextInput(attrs = {
				'id' : 'info',
				'class' : 'form-control',
				
				}),

		}