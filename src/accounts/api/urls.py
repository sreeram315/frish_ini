from django.conf.urls import url
from django.contrib import admin
from .views import ( 
						AccountCreateView, 
						AccountLoginView
				)



urlpatterns = [
    url(r'^create/$', AccountCreateView.as_view(), name = 'account-create'),
    url(r'^login/$', AccountLoginView.as_view(), name = 'account-login'),

    
]
