from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import CreateImageHostView, ImageDetailView



urlpatterns = [
	url(r'^$', CreateImageHostView.as_view(), name = 'imagehost-create'),
	url(r'^(?P<slug>[\w-]*)$', ImageDetailView.as_view(), name = 'imagehost-detail'),
]

