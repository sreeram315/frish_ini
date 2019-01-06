from django import template
from django.conf import settings

from blog.models import CommentsInfo
from accounts.models import AccountInfo


register = template.Library()

@register.filter(name = 'split')
def split(value, arg):
	if arg=='ent': arg='\n'
	return value.split(arg)

@register.filter(name = 'get_comm_replies')
def get_comm_replies(value):
	return CommentsInfo.objects.filter(parent = value)


@register.filter(name = 'users_name')
def users_name(value):
	return AccountInfo.objects.get(owner = value).name

@register.filter(name = 'users_slug')
def users_slug(value):
	return AccountInfo.objects.get(owner = value).slug

	

@register.filter(name = 'reply_count')
def reply_count(value):
	return CommentsInfo.objects.filter(parent = value).count()


