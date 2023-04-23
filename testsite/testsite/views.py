from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('страница index')


def blog(request, title):
    return HttpResponse(f'тема блога {title}')


def catalog(request, catid):
    print(request.GET) #http://127.0.0.1:8000/catalog/12/?name=Gagarina&cat=music
    return HttpResponse(f'<h1>Id в каталоге</h1>'
                        f'<p><h2>{catid}</h2>')
