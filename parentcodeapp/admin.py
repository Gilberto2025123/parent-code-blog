from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Comment, Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_at', 'author',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_at', 'author',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
