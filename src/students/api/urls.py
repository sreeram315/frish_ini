from django.conf.urls import url
from django.contrib import admin
from .views import ( StudentInfoListAPIView, StudentInfoDetailView, StudentInfoUpdateAPIView,
					 StudentInfoDeleteAPIView, StudentInfoCreateAPIView
					)



urlpatterns = [
    url(r'^all/$', StudentInfoListAPIView.as_view(), name = 'students-api'),
    url(r'^create/$', StudentInfoCreateAPIView.as_view(), name = 'students-api-create'),
    url(r'^(?P<slug>[\w-]+)/$', StudentInfoDetailView.as_view(), name = 'students-api-detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', StudentInfoUpdateAPIView.as_view(), name = 'students-api-update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', StudentInfoDeleteAPIView.as_view(), name = 'students-api-delete'),
    


]
