from django.shortcuts import render
from .models import category

# Create your views here.


def index(request):
    data=category.objects.all()
    print(data)
    return render(request,"index.html",{"data":data})
