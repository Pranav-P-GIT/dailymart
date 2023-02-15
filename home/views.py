from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"index.html")
def productlist(request):
    return render(request,"productlist.html")
def productpage(request):
    return render(request,"productpage.html")
def billing(request):
    return render(request,"billing.html")