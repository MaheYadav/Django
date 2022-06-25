from django.shortcuts import render

# def color1(request):
#     colors=["red","green","blue","yellow","white"]
#     return None

n=-1
def colorloop(request):

    colors = ["white","red", "green", "blue", "yellow"]
    # while True:
    #     return render(request,"colorloop.html",{"color1":colors[n]})

    for x in colors:
        return render(request,"colorloop.html",{"color1":x})


def color1(request):
    return render(request,"index.html",{"color":"white","link":"/color2/"})

def color2(request):
    return render(request,"index.html",{"color":"red","link":"/color3/"})

def color3(request):
    return render(request,"index.html",{"color":"green","link":"/color4/"})

def color4(request):
    return render(request,"index.html",{"color":"blue","link":"/color5/"})

def color5(request):
    return render(request,"index.html",{"color":"yellow","link":"/index/"})
