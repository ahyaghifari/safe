from django.shortcuts import render
from menu.models import Menu
# Create your views here.


def index(request):

    menu = Menu.objects.order_by('?')[:5]
    context = {
        'title': 'HOME',
        'menu': menu
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'TENTANG'})
