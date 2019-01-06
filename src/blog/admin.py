from django.contrib import admin

# Register your models here.
from .models import BlogInfo, CommentsInfo

admin.site.register(BlogInfo)

admin.site.register(CommentsInfo)


