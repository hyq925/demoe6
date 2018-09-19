from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account.models import *


def index(request):
    #导航
    navigations = Navigation.objects.all()
    #分类菜单
    categories = Category.objects.all()
    for category in categories:
        category.subs = category.submenu_set.all()
        for sub in category.subs:
            sub.subs2 = sub.submenu2_set.all()
        # 商品分类
        category.shops = category.shop_set.values('shop_id', 'name', 'promote_price')
        for shop in category.shops:
            shop.update(img=ShopImage.objects.filter(shop_id=shop.get('shop_id')).first())
    #轮播图
    banners = Banner.objects.all()

    # categories.shops=category.shop_set.values('shop_id','name','promote_price')
    # for shop in  categories.shops:
    #     img=ShopImage.objects.filter(shop_id=shop.get('shop_id')).first()
    #     shop.update(img)




    return render(request, 'index.html',
                  {'navigations': navigations, 'banners': banners, 'categories': categories})



