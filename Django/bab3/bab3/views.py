from django.http import HttpResponse

def tentang(request):
    return HttpResponse("Halaman Tentang")

def index(request):
    return HttpResponse("Hello, World di indeks")

