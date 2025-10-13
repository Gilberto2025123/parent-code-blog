from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = 'name', 'email', 'message', 'subject',
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Your Message',
            'subject': 'Subject',
        }
