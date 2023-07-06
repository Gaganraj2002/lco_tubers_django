from django.shortcuts import render,get_object_or_404
from .models import Youtuber
# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list("city",flat=True).distinct()
    camera_search = Youtuber.objects.values_list("camera_type",flat=True).distinct()
    category_search = Youtuber.objects.values_list("category",flat=True).distinct()

    data = {
        "tubers":tubers,
        "city_search":city_search,
        "camera_search":camera_search,
        "category_search":category_search
    }
    return render(request,"youtubers/youtubers.html",data)


def youtubers_id(request, id):
    tuber = get_object_or_404(Youtuber,pk=id)
    data = {
        "tuber":tuber
    }
    return render(request,"youtubers/youtuber_detail.html",data)
    


def search(request):
    tuber = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list("city",flat=True).distinct()
    camera_search = Youtuber.objects.values_list("camera_type",flat=True).distinct()
    category_search = Youtuber.objects.values_list("category",flat=True).distinct()

    if "Keyword" in request.GET:
        keyword = request.GET["Keyword"]
        if keyword:
            tuber= tuber.filter(description__icontains = keyword) 
            print(tuber)
    if 'city' in request.GET:
        city = request.GET["city"]
        if city and city!="City":
            tuber= tuber.filter(city__iexact = city) 
            print(tuber)
    if 'camera_type' in request.GET:
        camera = request.GET["camera_type"]
        if camera and camera!="Camera Type":
            tuber= tuber.filter(camera_type__iexact = camera) 
            print(tuber)
    if 'category' in request.GET:
        category = request.GET["category"]
        if category and category!="Category":
            tuber= tuber.filter(category__iexact = category) 
            print(tuber)
    
    data = {
        "tubers":tuber,
        "city_search":city_search,
        "camera_search":camera_search,
        "category_search":category_search
    }
    return render(request,"youtubers/key_search.html",data)

