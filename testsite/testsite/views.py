from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'testsite/index.html')


def blog(request, title):
    if title.startswith('z'):
        return redirect('myNewUrl', permanent=True)  # permanent=True перенесена постоянно
    return HttpResponse(f'тема блога {title}')


def catalog(request, catid):
    print(request.GET)  # http://127.0.0.1:8000/catalog/12/?name=Gagarina&cat=music
    if catid > 10:
        raise Http404()
    return HttpResponse(f'<h3>Id в каталоге</h3>'
                        f'<p><h1>{catid}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
