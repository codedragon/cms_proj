from django.contrib import admin
from cmsblog.models import Post
from cmsblog.models import Category


# Register your models here.
admin.site.register(Post)
admin.site.register(Category)