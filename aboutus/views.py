from django.shortcuts import render
from django.contrib import messages
from .models import AboutUs
from .models import ContactForm
# Create your views here.

def about_us():

    """
    Renders the About Us page
    """
    about = AboutUs.objects.all().order_by('-last_updated').first()

    return render(
        "aboutus/about_us.html",
        {"aboutus": about},
    )

def contact_us(request):
    from .forms import ContactForm as ContactFormModelForm 
    if request.method == "POST":
        contact_us_form = ContactFormModelForm(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for contacting Parent Code! We will get back to you shortly. Thank you!")
    return render(
        request,
        "aboutus/contact_us.html",
        {
            "contact_us": contact_us_form,
            "contact_form": contact_us_form,
        }
    )