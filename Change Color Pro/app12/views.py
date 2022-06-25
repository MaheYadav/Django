from django.shortcuts import render

def show(request):
    return render(request,"index.html",{"color":"#fa8072","link":"/changeClr/"})


def changeClr(request):
    return render(request,"index.html",{"color":"aqua","link":"/index/"})