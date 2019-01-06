from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.db.models import Q
from django.urls import reverse

# Create your models here.

from .utils import unique_slug_generator


User = settings.AUTH_USER_MODEL

def get_location(instance, filename):
	return f'imagehost_pictures/{instance.creater.username}/{filename}'



class ImageHostInfo(models.Model):
	creater				=	models.ForeignKey(User, on_delete = models.CASCADE)
	name				=	models.CharField(max_length = 100, null = True, blank = True)
	image				=	models.ImageField(upload_to = get_location,  null = True, blank = True, width_field="width_field", 
           										 height_field="height_field")
	height_field 		= 	models.IntegerField(default=0)
	width_field 		= 	models.IntegerField(default=0)
	slug				=	models.SlugField(null = True, blank  = True)



	def __str__(self):
		return str(self.image.name)

	@property
	def title(self):
		return self.image.name



	def get_absolute_url(self):
		return reverse('imagehost-detail',kwargs = {'slug':self.slug})



def stu_info_pre_save(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug	=	unique_slug_generator(instance)

pre_save.connect(stu_info_pre_save, sender = ImageHostInfo)
	

