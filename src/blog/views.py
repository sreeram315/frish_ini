from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ( TemplateView, ListView, DetailView, 
									CreateView, UpdateView, View, 
									FormView
								)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from urllib.request import urlopen
from django.db.models import Q, F
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.

from .forms import CreateBlogForm, TesterForm
from .models import BlogInfo, CommentsInfo
from .mixins import AjaxFormMixin
from accounts.models import AccountInfo

from students.api.serializers import StudentCreateSerializer


class BlogHome(ListView):
	template_name = 'blog/home.html'
	paginate_by = 10

	def get_queryset(self):
		query 							=	self.request.GET.get('q')
		genre 							=	self.request.GET.get('genre')

		if not query: query = ''
		if not genre: genre = ''

		if any([query, genre]):
			blogs = BlogInfo.objects.search(query, genre)
			return blogs
		else:
			return BlogInfo.objects.all().order_by('-last_updated')



class BlogCreateView(LoginRequiredMixin, CreateView):
	login_url 	=	'/login/'
	template_name = 'blog/create.html'
	form_class = CreateBlogForm


	def form_valid(self, form):
		form = CreateBlogForm(self.request.POST or None, self.request.FILES or None)
		instance 		= form.save(commit = False)
		instance.creater 	= self.request.user
		return super(BlogCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context 			= super(BlogCreateView, self).get_context_data(*args, **kwargs)
		context['title']	= 'New Blog'
		context['genre_option_list']	=	['INSPIRATIONAL','EDUCATIONAL','ENTERTAINMENT','NEWS']
		return context

class BlogUpdateView(LoginRequiredMixin, UpdateView):
	template_name 	= 	'blog/update.html'
	form_class 		=	CreateBlogForm
	login_url		=	'/login/'
	queryset		=	BlogInfo.objects.all()

	def get_context_data(self, *args, **kwargs):
		context 			= super(BlogUpdateView, self).get_context_data(*args, **kwargs)
		context['title']	= 'Update Blog'
		context['genre_option_list']	=	['INSPIRATIONAL','EDUCATIONAL','ENTERTAINMENT','NEWS']
		return context



class BlogDetailView(DetailView):
	template_name = 'blog/detail.html'
	queryset 	  = BlogInfo.objects.all()

	def get_context_data(self, *args, **kwargs):
		context 			= super(BlogDetailView, self).get_context_data(*args, **kwargs)
		context['user'] 	= AccountInfo.objects.get(owner = BlogInfo.objects.get(slug = self.kwargs['slug']).creater)
		comments 			= CommentsInfo.objects.filter(blog = BlogInfo.objects.get(slug = self.kwargs['slug']), parent =  None)
		
		context['comments']	=	comments
		return context

	def post(self, request,  *args, **kwargs):
		if self.request.is_ajax():
			if request.POST.get('comment_content'):
				CommentsInfo.objects.create(
									creater = request.user,
									content = request.POST.get('comment_content'),
									blog   	= BlogInfo.objects.get(slug = self.kwargs['slug']),
									is_parent	=	True
								)
			elif request.POST.get('reply'):
				reply		=	request.POST.get('reply')
				parent_slug	=	request.POST.get('parent')
				CommentsInfo.objects.create(
									creater = request.user,
									content = reply,
									blog   	= BlogInfo.objects.get(slug = self.kwargs['slug']),
									parent  = CommentsInfo.objects.filter(slug=parent_slug).first(),
									is_parent = False
								)
				data = {
				'message': "Successfully submitted forum data."
				}
				return JsonResponse(data)
		else:
			return HttpResponseRedirect('/')


from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

class CommentLikeAPIToggle(APIView):
	authentication_classes 	= [authentication.SessionAuthentication]
	permission_classes 		= [permissions.IsAuthenticated]

	def get(self, request, slug = None, format = None):
		obj = get_object_or_404(CommentsInfo, slug = slug)
		url_ = obj.get_absolute_url()
		user = self.request.user
		toggled , liked = False, False
		if user.is_authenticated:
			if user not in obj.likes.all():
				obj.likes.add(user)
				liked = True
			else:
				obj.likes.remove(user)
			toggled = True
		
		data = {
				'toggled': toggled,
				'liked' : liked
		}

		return Response(data)

class CommentAPILikedUsers(APIView):

	def get(self, request, slug = None, format = None):
		obj = get_object_or_404(CommentsInfo, slug = slug)
		user = request.user
		if user.is_authenticated:
			liked_users, user_links = [], []
			likedusers = obj.likes.all()
			for user in likedusers:
				acc_obj = AccountInfo.objects.filter(owner = user).first()

				if acc_obj.name: liked_users.append(acc_obj.name)
				else: liked_users.append(user.username)

				link_slug = acc_obj.slug
				link = reverse(f'account-profile', kwargs = {'slug': link_slug})
				user_links.append(link)

		
		
		data = {
				'liked_users': liked_users,
				'user_links': user_links
		}

		print(f"""


			data:	{data}



			""")

		return Response(data)




class TesterView(TemplateView):
	template_name = 'tester.html'
	# form_class = TesterForm
	# success_url = '/'

	# def get_context_data(self):
	# 	data = {
	# 		'name': 'kaala charan b',
	# 		'reg_no': 11291311,
	# 		'section': 'e1334',
	# 		'cgpa'	:	10,
	# 		'gender': 'M'
	# 	}

	# 	ser = StudentCreateSerializer(data = data, partial = True)

	# 	if ser.is_valid():
	# 		ser.save()

	

	 # def get_queryset(self):
	 # 	return BlogInfo.objects.all()

	 # def get_context_data(self):
	 # 	context = super(TesterView, self).get_context_data()
	 # 	return context





		
























