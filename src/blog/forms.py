from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.core.exceptions import ValidationError
from pagedown.widgets import PagedownWidget
#
from .models import BlogInfo

User 	= get_user_model()

class BlogForm(forms.Form):
	headline			=	forms.CharField(required = False)
	content				=	forms.CharField(required = False)
	image				=	forms.ImageField(required = False)
	genre 				=	forms.CharField(required = False)
	preview_points 		=	forms.CharField(required = False)
	age_restricted		=	forms.BooleanField(required = False)
	use_editor 			=	forms.BooleanField(required = False)


class CreateBlogForm(forms.ModelForm):

	content 	= forms.CharField(widget = PagedownWidget(show_preview = False), required = False)
	ocontent 	= forms.CharField(label = 'ocontent', required = False)

	class Meta:
		fields = '__all__'
		model = BlogInfo
		fields = ('use_editor', 'headline', 'age_restricted', 'content', 'image', 'genre', 'preview_points', 'ocontent' )

	def clean_headline(self):
		hl 	=	self.cleaned_data.get('headline')
		if not hl or len(hl) < 2:
			raise ValidationError('Headline length cannot be so less')
		return hl

	def clean_preview_points(self):
		pp 	= self.cleaned_data.get('preview_points')
		if pp and len(pp.split('\n')) > 3:
			raise ValidationError('Preview points cannot be more than three')
		else:
			return pp

	def clean_content(self):
		used_editor = self.cleaned_data.get('use_editor')
		ocontent = self.data.get('ocontent')
		if used_editor:
			content =  self.data.get('content')
		else:
			content = ocontent
		if len(content) == 0: raise ValidationError('Write something')
		return content

class TesterForm(forms.ModelForm):
	name = forms.CharField(label = 'Full name', required = True)
	contact = forms.CharField(label = 'Contact', required = True)

	class Meta:
		model = BlogInfo
		fields = [
					'name',
					'contact'
				 ]

	def clean_name(self):
		value = self.cleaned_data['name']
		if value == 'hello':
			raise ValidationError('Not a valid name')
		return value

	









