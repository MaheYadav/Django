from django.http import HttpResponse
from django.shortcuts import render
from app11.models import Producce

# Create your views here.
def show(request):
    return render(request,"index.html")


def savedata(request):
    no=request.POST.get("no")
    name=request.POST.get("name")
    price=request.POST.get("price")
    image=request.FILES["image"]
    print(no,name,price,image)
    Producce(p_no=no,p_name=name,p_price=price,p_image=image).save()
    data=Producce.objects.all()
    print(data)
    return render(request, 'index.html', {'data':data})
    #return HttpResponse("save")


def dataIndex(request):
   s= Producce.objects.all()
   print(s)
   return render(request,"index.html",{'pro':s})


def deletedata(request):
    idno=request.GET.get("p_no")
    Producce.objects.filter(p_no=idno).delete()
    Producce.objects.all()
    return render(request,"index.html" )
