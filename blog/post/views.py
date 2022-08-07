from django.shortcuts import render

# Create your views here.


def index(request):
    path = request.GET.get('query', "hech narsa junatilmadi!!!")
    return render(request, 'index.html', {"value": path})
