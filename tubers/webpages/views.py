from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    youtuber = Youtuber.objects.order_by(
        "-created_date")
    featured_youtuber = Youtuber.objects.order_by(
        "-created_date").filter(is_featured=True)
    teams = Team.objects.all()
    data = {
        "sliders": sliders,
        "teams": teams,
        "fy": featured_youtuber,
        "yts": youtuber
    }
    return render(request, "webpages/home.html", data)


def about(request):
    teams = Team.objects.all()
    data = {
        "teams": teams
        }
    return render(request, "webpages/about.html",data)


def services(request):
    return render(request, "webpages/services.html")


def contact(request):
    return render(request, "webpages/contact.html")
