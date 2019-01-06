from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model

from django.utils.safestring import mark_safe
from markdown_deux import markdown


# Create your models here.

from .utils import unique_slug_generator


User = settings.AUTH_USER_MODEL
users =  get_user_model()

def get_location(instance, filename):
	return f'blog_pictures/{instance.creater.username}/{filename}'

class BlogInfoManager(models.Manager):
	def search(self, query = '', genre = ''):
		return BlogInfo.objects.filter(
											Q(headline__icontains = query)|
											Q(creater__username__icontains = query),
											genre__icontains	=	genre

									).order_by(
									'-last_updated'
								)



class BlogInfo(models.Model):
	INSPIRATIONAL 		= 'INSPIRATIONAL'
	EDUCATIONAL			= 'EDUCATIONAL'
	ENTERTAINMENT 		= 'ENTERTAINMENT'
	NEWS 				= 'NEWS'

	GENRE = (
        (INSPIRATIONAL, 'Inspirational'),
        (EDUCATIONAL, 	'Educational'),
        (ENTERTAINMENT, 'Entertainment'),
        (NEWS, 			'News'),
    )

	creater				=	models.ForeignKey(User, on_delete = models.CASCADE)
	headline			=	models.CharField(max_length = 1000, null = True, blank = True)
	preview_points		=	models.TextField(blank = True, null = True)
	date_time			=	models.DateTimeField(blank = True, null = True, auto_now_add = True)
	last_updated		=	models.DateTimeField(blank = True, null = True, auto_now = True)
	age_restricted		=	models.BooleanField(default = False)
	content				=	models.TextField(blank = True, null = True)
	image				=	models.ImageField(upload_to = get_location,  null = True, blank = True, width_field="width_field", 
           										 height_field="height_field")
	height_field 		= 	models.IntegerField(default=0)
	width_field 		= 	models.IntegerField(default=0)
	slug 				=	models.SlugField(null = True, blank  = True)
	genre 				=	models.CharField(
										        max_length=20,
										        choices=GENRE,
										        default=NEWS,
										    )
	likes				=	models.IntegerField(default = 0)
	use_editor 			=	models.BooleanField(default = False)


	objects = BlogInfoManager()

	def __str__(self):
		return str(self.headline)

	@property
	def title(self):
		return self.headline


	def get_absolute_url(self):
		return f'/blog/{self.slug}'

	def marked_content(self):
		content = self.content
		return mark_safe(markdown(content))


def blog_info_pre_save(sender, instance, *args, **kwargs):
	print('saving--------saving')
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
	instance.content = '\n' + instance.content

pre_save.connect(blog_info_pre_save, sender = BlogInfo)



class CommentsInfo(models.Model):
	creater				=	models.ForeignKey(User, on_delete = models.CASCADE)
	blog 				=	models.ForeignKey(BlogInfo, on_delete = models.CASCADE)
	content				=	models.CharField(max_length = 5000, null = True, blank = True)
	date_time			=	models.DateTimeField(null = True, blank = True, auto_now_add = True)
	likes				=	models.ManyToManyField(User, blank = True, related_name = 'liking')
	slug 				=	models.SlugField(null = True, blank  = True)
	parent				=	models.ForeignKey('self', blank = True, null = True, on_delete = models.CASCADE)
	is_parent			=	models.BooleanField(default = False)


	def get_api_like_toggle(self):
		return f'/blog/api/comment/like/{self.slug}'

	def get_absolute_url(self):
		blog_slug = self.blog.slug
		return f'/blog/{blog_slug}'

	def get_liked_users_url(self):
		return f'/blog/api/comment/liked-users/{self.slug}'

	

	@property
	def title(self):
		return self.content

	def __str__(self):
		return self.content
		return 'okok'
		return f'{self.creater} // {self.date_time.date()} // {self.content[:10]}'





def comment_info_pre_save(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(comment_info_pre_save, sender = CommentsInfo)
	

