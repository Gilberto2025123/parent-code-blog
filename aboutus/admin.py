from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import AboutUs, ContactForm


@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
