from django.shortcuts import render

from app18.models import Product

def showAll(req):
    all_products=Product.objects.all()
    return render(req,"index.html",{"data":all_products})

def askData(request):
    return showAll(request)

def saveData(request):
    p_no=request.POST.get("no")
    a=Product.objects.filter(no=p_no)
    print(a,"..",type(a))
    # if a==<QuerySet []>:
    #     print("new product is registered")
    #     msg="new product is registered"
    # else:
    #     print("existing product is updated")
    #     msg="existing product is updated"
    # #b=Product.objects.get(no=p_no)
    p_name=request.POST.get("name")
    p_price=request.POST.get("price")
    p_image=request.FILES.get("image")
    Product(no=p_no,name=p_name,price=p_price,image=p_image).save()
    return showAll(request)
    # all_products=Product.objects.all()
    # return render(request,"index.html",{"data":all_products,"msg":msg})

def deleteProduct(request):
    pno=request.GET.get("pno")
    Product.objects.filter(no=pno).delete()
    return showAll(request)


def updateProduct(request):
    pn=request.GET.get("pn")
    print(pn)
    res=Product.objects.get(no=pn)
    all_products=Product.objects.all()
    return render(request,"index.html",{"update":res,"data":all_products})