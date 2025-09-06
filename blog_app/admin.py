from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','user','pub_date','tag']
    ordering = ['title','-pub_date']
    search_fields = ['title','cotent']
    prepopulated_fields = {'slug':['title','tag']}
    list_editable = ['tag']