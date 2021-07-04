from django import forms

from .models import Closure, Bordereaux


class ClosureForm(forms.ModelForm):
	class Meta:
		model = Closure
		fields = [
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
				'class' : 'form-control'
				}),
			'closure_money' : forms.NumberInput(attrs={
				'id':'clo_mny',
				'class' : 'form-control'
				}),
			'closure_paper' : forms.NumberInput(attrs={
				'id':'clo_pper',
				'class' : 'form-control'
				}),
			'money' : forms.NumberInput(attrs={
				'id':'mny',
				'class' : 'form-control'
				}),
			'details' : forms.TextInput(attrs={
				'id':'dtls',
				'class' : 'form-control'
				}),
			'wasfa' : forms.NumberInput(attrs={
				'id':'wasfa',
				'class' : 'form-control'
				})


		}

		labels = {
			'start_money' : ("Monais D'Ouverture"),
			'closure_money' : ("Monais de Cloture"),
			'closure_paper' : ("Biais de Cloure"),
			'money' : ("Ecart Connu"),
			'details' : ("Details d'Ecart"),
			'wasfa' : ("Somme Sur Logiciel de Gestion"),

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


class BordereauxForm(forms.ModelForm):
	class Meta:
		model = Bordereaux
		fields = ['pay_ctr','n_brd','dt_clo','n_ord','m_brd','dt_depot']
		CTR_CHOICES = (
			('', ''),
			('CNAS','CNAS'),
			('CASNOS','CASNOS'),
			('Caisse Militaire','Caisse Militaire'))
		widgets = {
			'pay_ctr' : forms.Select(choices=CTR_CHOICES, attrs={
				'id' : 'ctr',
				'class' : 'form-control',
				
				'label' : 'Centre de Payment'
				}),
			'n_brd' : forms.NumberInput(attrs={
				'id' : 'nbrd',
				'class' : 'form-control',
				
				}),
			'dt_clo' : forms.DateInput(attrs={
				'id' : 'dt_clo',
				'class' : 'form-control',
				
				'type' : 'date'
				}),
			'n_ord' : forms.NumberInput(attrs={
				'id' : 'nord',
				'class' : 'form-control',
				
				}),
			'm_brd' : forms.NumberInput(attrs={
				'id' : 'mbrd',
				'class' : 'form-control',
				
				}),
			'dt_depot' : forms.DateInput(attrs={
				'id' : 'dtdepot',
				'class' : 'form-control',
				'type' : 'date',
				'required' : 'True'
				}),
		}
		labels = {
			'pay_ctr' : ("Centre Payement"),
			'n_brd' : ("N° Brd"),
			'dt_clo' : (" Date Cloture"),
			'n_ord' : ("Nbr Ord "),
			'm_brd' : ("Montant Brd"),
			'dt_depot' : ("Date Depot"),
			# 'dt_jrl' : ("Date du Journal"),
			# 'n_ord_jrl' : ("Nombre d'Ordenance du Journal"),
			# 'm_jrl' : ("Montant du Journal")


		}


class EditBrdFrom(forms.ModelForm):
	class Meta:
		model = Bordereaux
		fields = ['pay_ctr', 'n_brd', 'dt_clo', 'n_ord','m_brd', 'dt_depot', 'dt_jrl', 'n_ord_jrl', 'm_jrl', "payement"]
		CTR_CHOICES = (
			('', ''),
			('CNAS','CNAS'),
			('CASNOS','CASNOS'),
			('Caisse Militaire','Caisse Militaire'))
		widgets = {
			'pay_ctr' : forms.Select(choices=CTR_CHOICES, attrs={
				'id' : 'ctr',
				'class' : 'form-control',
				}),
			'n_brd' : forms.NumberInput(attrs={
				'id' : 'nbrd',
				'class' : 'form-control',
				}),
			'dt_clo' : forms.DateInput(attrs={
				'id' : 'dt_clo',
				'type' : 'date',
				'class' : 'form-control',
				}),
			'n_ord' : forms.NumberInput(attrs={
				'id' : 'nord',
				'class' : 'form-control',
				}),
			'm_brd' : forms.NumberInput(attrs={
				'id' : 'mbrd',
				'class' : 'form-control',
				}),
			'dt_depot' : forms.DateInput(attrs={
				'id' : 'dtdepot',
				'type' : 'date',
				'class' : 'form-control',
				}),
			'dt_jrl' : forms.DateInput(attrs={
				'id' : 'dt_jrl',
				'type' : 'date',
				'class' : 'form-control',
				'required' : 'True'
 				}),
			'n_ord_jrl' : forms.NumberInput(attrs={
				'id' : 'n_ord_jrl',
				'class' : 'form-control',
	
				}),
			'm_jrl' : forms.NumberInput(attrs={
				'id' : 'm_jrl',
				'class' : 'form-control',

				})
			}
		labels = {
			'pay_ctr' : ("Payement center"),
			'n_brd' : ("Slip Number : "),
			'dt_clo' : (" Slip Closing Date"),
			'n_ord' : ("Prescription Number (Slip)"),
			'm_brd' : ("Slip Amount"),
			'dt_depot' : ("Diposit Date(Slip)"),
			'dt_jrl' : ("Sheet Date"),
			'n_ord_jrl' : ("Prescription Number(Sheet)"),
			'm_jrl' : ("Sheet Amount"),
			'payement': ('Payed?...')


		}

