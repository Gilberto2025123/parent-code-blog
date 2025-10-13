from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_us, name='aboutus'),
    path('contact/', views.contact_us, name='contact_us'),
]