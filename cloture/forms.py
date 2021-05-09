from django import forms

from .models import Closure


class ClosureForm(forms.ModelForm):
	class Meta:
		model = Closure
		fields = [
			'username',
			'start_money',
			'closure_money',
			'closure_paper',
			'money',
			'details',
			'wasfa'
		]


		widgets = {
			'start_money' : forms.NumberInput(attrs={
				'id':'str_mny',
				'class' : 'input',
				'placeholder' : "L'argent de Demarrage"
				}),
			'closure_money' : forms.NumberInput(attrs={
				'id':'clo_mny',
				'class' : 'input',
				'placeholder' : "L'argent de Cloture"
				}),
			'closure_paper' : forms.NumberInput(attrs={
				'id':'clo_pper',
				'class' : 'input',
				'placeholder' : "Biais de Cloture"
				}),
			'money' : forms.NumberInput(attrs={
				'id':'mny',
				'class' : 'input',
				'placeholder' : "La somme d'ecart"
				}),
			'details' : forms.TextInput(attrs={
				'id':'dtls',
				'class' : 'input',
				'placeholder' : "Details d'ecart"
				}),
			'wasfa' : forms.NumberInput(attrs={
				'id':'wasfa',
				'class' : 'input',
				'placeholder' : "Somme de Wasfa"
				})


		}



class PartielClosureForm(forms.ModelForm):
	class Meta:
		model = Closure
		fields = ['money', 'details']
		widgets = {
			'money' : forms.NumberInput(attrs={
				'id':'mny',
				'class' : 'input',
				'placeholder' : "La somme d'ecart"
				}),
			'details' : forms.TextInput(attrs={
				'id':'dtls',
				'class' : 'input',
				'placeholder' : "Details d'ecart"
				}),}