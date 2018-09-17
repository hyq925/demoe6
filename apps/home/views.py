from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account.models import Navigation, Category, Banner


def index(request):
    navigations = Navigation.objects.all()
    categories = Category.objects.all()
    for category in categories:
        category.subs = category.submenu_set.all()
        for sub in category.subs:
            sub.subs2 = sub.submenu2_set.all()
    banners = Banner.objects.all()
    return render(request, 'index.html',
                  {'navigations': navigations, 'banners': banners, 'categories': categories})



