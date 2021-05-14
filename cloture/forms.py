from django import forms

from .models import Closure, Bordereaux


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
			'username' : forms.Select(attrs={
				'id':'str_mny',
				'class' : 'form-control'
				}),
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
			'username' : ("Nom d'utilisateur"),
			'start_money' : ("L'Argent de Demarrage"),
			'closure_money' : ("L'Argent de Cloture"),
			'closure_paper' : ("Biais de Cloture"),
			'money' : ("Reglage d'Ecart"),
			'details' : ("Details Sur L'Ecart"),
			'wasfa' : ("Montant Sur Logiciel"),

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
			'pay_ctr' : ("Centre de Payement"),
			'n_brd' : ("Numero de Bordereau"),
			'dt_clo' : ("Date de Cloture du Bordereau"),
			'n_ord' : ("Nombre d'Ordenance du Bordereau"),
			'm_brd' : ("Montant du Bordereau"),
			'dt_depot' : ("date de Depot Du Bordereau"),
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
			'pay_ctr' : ("Centre de Payement"),
			'n_brd' : ("Numero de Bordereau"),
			'dt_clo' : ("Date de Cloture du Bordereau"),
			'n_ord' : ("Nombre d'Ordenance du Bordereau"),
			'm_brd' : ("Montant du Bordereau"),
			'dt_depot' : ("date de Depot Du Bordereau"),
			'dt_jrl' : ("Date du Journal"),
			'n_ord_jrl' : ("Nombre d'Ordenance du Journal"),
			'm_jrl' : ("Montant du Journal"),
			'payement': ('Payé?...')


		}