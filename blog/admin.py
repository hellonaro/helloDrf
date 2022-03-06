from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag, Comment

blogModels = [Post, Category, Tag, Comment]
admin.site.register(blogModels)