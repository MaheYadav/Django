from django.shortcuts import render

def login(request):
    return render(request,"login.html")

def loginCheck(request):
    uname=request.POST.get("t1")
    upassword=request.POST.get("t2")
    if uname=="Mahi" and upassword=="1188":
        return render(request,"welcome.html")
    error="*invalid username or password"
    return render(request,"login.html",{"msg":error})