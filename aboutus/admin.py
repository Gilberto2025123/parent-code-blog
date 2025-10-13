from django.contrib import admin
from .models import AboutUs, ContactForm
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)