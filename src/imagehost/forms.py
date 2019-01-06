from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.core.exceptions import ValidationError
#
from .models import ImageHostInfo

User 	= get_user_model()

class CountForm(forms.Form):
	name				=	forms.CharField(required = False)
	image				=	forms.ImageField(required = True)


class ImageCreateForm(forms.ModelForm):
	name				=	forms.CharField(label = 'What\'s in this Image(Optional)', 	
												widget=forms.TextInput(attrs={'placeholder': 'Optional'}),			
												required = False)
	image				=	forms.ImageField(label = 'Image', required = True)

	class Meta:
		model = ImageHostInfo
		fields = ('name', 'image')


		
