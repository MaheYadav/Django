from django.http import HttpResponse

def show(request):
    msg="hello world"
    return HttpResponse(msg)


def display(req):
    a="<html><body><h1>hey google</h1></body></html>"
    return HttpResponse(a)
    
