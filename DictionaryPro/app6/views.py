from django.shortcuts import render

def showIndex(request):
    d1={
        "101":{"name":"Ravi","salary":125000.00},
        "102": {"name": "Kumar", "salary": 185000.00},
        "103": {"name": "Mohan", "salary": 275000.00}
        }
    return render(request,"index.html",{"data":d1})