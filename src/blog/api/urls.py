from django.conf.urls import url
from django.contrib import admin
from .views import ( PostListAPIView, 		# blogs


					CommentCreateView		# comments
				)



urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name = 'blog-api'),		# blogs

     url(r'^comment/create$', CommentCreateView.as_view(), name = 'blog-api-comment-create'), 		# comments
]
