from django.shortcuts import render

def showIndex(request):
    d1={"idno":101,"name":"Ravi","salary":125000.00}
    return render(request,"index.html",d1)