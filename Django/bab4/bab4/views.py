from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, my name is Ridwan</h1>")