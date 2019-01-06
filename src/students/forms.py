from django import forms
import re
from django.core.exceptions import ValidationError
from .models import StudentInfo

class StudentAddForm(forms.Form):
	reg_no		=	forms.IntegerField()
	name		=	forms.CharField(required = False)
	cgpa		=	forms.FloatField()
	dob			=	forms.DateField()
	section		=	forms.CharField(required = False)
	contact		=	forms.IntegerField(required = False)
	batch		=	forms.IntegerField(required = False)
	address		=	forms.CharField(required = False)
	department	=	forms.CharField(required = False)
	updated		=	forms.DateTimeField(required = False)
	slug		=	forms.SlugField(required = False)
	description	=	forms.CharField(required = False)



class StudentInfoCreateForm(forms.ModelForm):

	name 			= forms.CharField(		label = 'Name',
											widget=forms.TextInput(attrs={'placeholder': 'Jonathan Thakur'}),
											required = False
										)
	address			= forms.CharField(
									        label='Address',
									        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}),
									        required = False
									    )
	cgpa			= forms.CharField( 		label = 'CGPA', 
											widget=forms.TextInput(attrs={'placeholder': '9.76'}),
									        required = False
									    )

	class Meta:
		model = StudentInfo
		fields =  [
			'name', 'reg_no', 'cgpa', 'dob', 'section', 'contact', 'batch', 'address', 'department', 'description'
		]

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == None or len(name) <= 2:
			raise ValidationError('Not a valid name')
		return name

	def clean_section(self):
		section = self.cleaned_data.get('section')
		if section and not bool(re.match(r'[a-zA-Z]{1,3}\d+$', section)):
			raise ValidationError('Not a valid section')
		return section