from django.shortcuts import render
from .models import product

# Create your views here.
def productlist(request):
    id=request.GET["id"]
    data=product.objects.filter(cate_id=id)
    return render(request,"productlist.html",{"data":data})



def productpage(request):
    id=request.GET["id"]
    data=product.objects.get(id=id)
    total = int(data.price)-(int(data.price)*int(data.discount)/100)
    return render(request,"productpage.html",{"data":data, "total":total})



def billing(request):
        id=request.GET["id"]
        
        if request.method=="POST":
            q=request.POST["q"]
            data=product.objects.get(id=id)
            total1 =int(data.price)-(int(data.price)*int(data.discount)/100)
            total2 =int(total1)*int(q)
        return render(request,"billing.html",{"data":data, "total1":total1,"q":q,"total2":total2})
    
    
def thankyou(request):
    return render(request,"thankyou.html",)