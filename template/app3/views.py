from django.shortcuts import render
def showHtmlPage(request):
    return render(request,"main.html")
