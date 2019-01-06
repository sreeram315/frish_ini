from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import (BlogHome, BlogCreateView,BlogUpdateView,  
						BlogDetailView, TesterView, CommentLikeAPIToggle,
						CommentAPILikedUsers,
						)



urlpatterns = [

	url(r'^b/$', TesterView.as_view(), name = 'blog-tester'),	

	url(r'^$', BlogHome.as_view(), name = 'blog-home'),
	url(r'^create/$', BlogCreateView.as_view(), name = 'blog-create'),
	url(r'^update/(?P<slug>[\w-]*)/$', BlogUpdateView.as_view(), name = 'blog-update'),
	url(r'^(?P<slug>[\w-]*)/$', BlogDetailView.as_view(), name = 'blog-detail'),





	url(r'^api/comment/like/(?P<slug>[\w-]*)/$', CommentLikeAPIToggle.as_view(), name = 'blog-comment-like-toggle'),
	url(r'^api/comment/liked-users/(?P<slug>[\w-]*)/$', CommentAPILikedUsers.as_view(), name = 'blog-comment-like-toggle'),

	






	
]

