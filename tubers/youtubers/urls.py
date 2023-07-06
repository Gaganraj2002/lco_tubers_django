from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.youtubers, name="youtubers"),
    path('<int:id>', views.youtubers_id, name="youtubers_id"),
    path('search', views.search, name="search"),
]
