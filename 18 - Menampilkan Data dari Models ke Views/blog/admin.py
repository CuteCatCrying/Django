from django.contrib import admin

# Register your models here.
from .models import Post
# from . import models

admin.site.register(Post)
# admin.site.register(models.Post)
