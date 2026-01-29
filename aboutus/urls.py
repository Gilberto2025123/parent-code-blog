from django.urls import path

from . import views

# URL patterns for About Us section
urlpatterns = [
    # About Us page - tells visitors about Parent Code
    path('', views.about_us, name='aboutus'),
    # Contact form page
    path('contact/', views.contact_us, name='contact_us'),
    # Landing page (also accessible from root URL)
    path('landing/', views.landing_page, name='landing_page'),
]
