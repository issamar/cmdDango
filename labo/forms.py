from .models import Labo
from django import forms


class LaboForm(forms.ModelForm):
	class Meta:
		model = Labo
		fields = '__all__'

		labels = {
			'dt' : ('Blood Sample Date '),
			'p_name' : ('Patiente Name '),
			'dob' : ('Date Of Birth '),
			'params' : ('The Achieved Analysis'),
			'lab_price' : (''),
			'price' : ('Price '),
			'pay' : ('Payement'),
			'rest' : ('The Rest '),
			'info' : ('Additionnal Informations ')
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