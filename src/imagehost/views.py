from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, View
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from urllib.request import urlopen
from django.urls import reverse

# Create your views here.

from .forms import ImageCreateForm
from .models import ImageHostInfo


class CreateImageHostView(LoginRequiredMixin, CreateView):
	login_url		=	'/login/'
	form_class 		= 	ImageCreateForm
	template_name 	= 	'imagehost/create.html'	

	def form_valid(self, form):
		form 					= ImageCreateForm(self.request.POST or None, self.request.FILES or None)
		instance 				= form.save(commit = False)
		instance.creater 		= self.request.user
		print('----------\nsaving\n--------')
		return super(CreateImageHostView, self).form_valid(form)


class ImageDetailView(DetailView):
	queryset	=	ImageHostInfo.objects.all()
	template_name = 'imagehost/detail.html'

