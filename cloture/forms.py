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


class BordereauxForm(forms.ModelForm):
	class Meta:
		model = Bordereaux
		fields = ['pay_ctr','n_brd','dt_clo','n_ord','m_brd','dt_depot']
		widgets = {
			'pay_ctr' : forms.TextInput(attrs={
				'id' : 'ctr',
				'class' : 'input',
				'placeholder' : 'Centre Payeur',
				'label' : 'Centre de Payment'
				}),
			'n_brd' : forms.NumberInput(attrs={
				'id' : 'nbrd',
				'class' : 'input',
				'placeholder' : 'Numero de Bordereau'
				}),
			'dt_clo' : forms.DateInput(attrs={
				'id' : 'dt_clo',
				'class' : 'input',
				'placeholder' : 'Date de Cloture',
				'type' : 'date'
				}),
			'n_ord' : forms.NumberInput(attrs={
				'id' : 'nord',
				'class' : 'input',
				'placeholder' : 'Nombre des Ord'
				}),
			'm_brd' : forms.NumberInput(attrs={
				'id' : 'mbrd',
				'class' : 'input',
				'placeholder' : 'Montant de Bordereau'
				}),
			'dt_depot' : forms.DateInput(attrs={
				'id' : 'dtdepot',
				'class' : 'input',
				'placeholder' : 'Date de depot',
				'type' : 'date'
				}),
		}


class EditBrdFrom(forms.ModelForm):
	class Meta:
		model = Bordereaux
		fields = ['pay_ctr', 'n_brd', 'dt_clo', 'n_ord','m_brd', 'dt_depot', 'dt_jrl', 'n_ord_jrl', 'm_jrl', "payement"]
		widgets = {
			'pay_ctr' : forms.TextInput(attrs={
				'id' : 'ctr',
				'class' : 'input',
				'placeholder' : 'Centre Payeur',
				'label' : 'Centre de Payment'
				}),
			'n_brd' : forms.NumberInput(attrs={
				'id' : 'nbrd',
				'class' : 'input',
				'placeholder' : 'Numero de Bordereau'
				}),
			'dt_clo' : forms.DateInput(attrs={
				'id' : 'dt_clo',
				'class' : 'input',
				'placeholder' : 'Date de Cloture',
				'type' : 'date'
				}),
			'n_ord' : forms.NumberInput(attrs={
				'id' : 'nord',
				'class' : 'input',
				'placeholder' : 'Nombre des Ord'
				}),
			'm_brd' : forms.NumberInput(attrs={
				'id' : 'mbrd',
				'class' : 'input',
				'placeholder' : 'Montant de Bordereau'
				}),
			'dt_depot' : forms.DateInput(attrs={
				'id' : 'dtdepot',
				'class' : 'input',
				'placeholder' : 'Date de depot',
				'type' : 'date'
				}),
			'dt_jrl' : forms.DateInput(attrs={
				'id' : 'dt_jrl',
				'class' : 'input',
				'type' : 'date'
 				}),
			'n_ord_jrl' : forms.NumberInput(attrs={
				'id' : 'n_ord_jrl',
				'class' : 'input',
				'placeholder' : 'N° ord Du Journal'
				}),
			'm_jrl' : forms.NumberInput(attrs={
				'id' : 'm_jrl',
				'class' : 'input',
				'placeholder' : 'Montant de Journal'
				})
			}