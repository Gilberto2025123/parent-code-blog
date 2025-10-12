from django.shortcuts import render
from .models import AboutUs
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

