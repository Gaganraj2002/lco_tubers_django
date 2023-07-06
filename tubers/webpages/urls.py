from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="Home"),
    path('about', views.about, name="About"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="Contact"),
]
