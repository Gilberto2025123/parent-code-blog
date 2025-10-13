from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AboutUs, ContactForm
from .forms import ContactFormModelForm
# Create your views here.

def about_us(request):

    """
    Renders the About Us page
    """
    about = AboutUs.objects.all().order_by('-last_updated').first()

    return render(
        request,
        "aboutus/about_us.html",
        {"aboutus": about},
    )

def contact_us(request):
     
    contact_us_form = ContactFormModelForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and contact_us_form.is_valid():
        contact_us_form.save()
        messages.add_message(request, messages.SUCCESS, "Thank you for contacting Parent Code! We will get back to you shortly.")
        return redirect('contact_us')

    return render(
        request,
        "aboutus/contact_us.html",
        {
            "contact_us_form": contact_us_form,
        }
    )
    