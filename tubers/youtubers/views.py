from django.shortcuts import render,get_object_or_404
from .models import Youtuber
# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.all()
    data = {
        "tubers":tubers
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
    if "Keyword" in request.GET:
        keyword = request.GET["Keyword"]
        if keyword:
            tuber= tuber.filter(description__icontains = keyword) 
            print(tuber)
    data = {
        "tubers":tuber
    }
    return render(request,"youtubers/key_search.html",data)

