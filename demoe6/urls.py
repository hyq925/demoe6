import xadmin
from django.conf.urls import url,include

from home import views

urlpatterns = [
    url('xadmin/', xadmin.site.urls),

    #xadmin
    url('account/',include('account.urls')),
    #首页
    url('^$',views.index),
    #apps项目
    url('home/',include('home.urls')),
    url('order/',include('order.urls')),
    url('pay/',include('pay.urls')),
    url('shopcar/',include('shopcar.urls')),
    url('search/',include('search.urls')),
    url('shop_detail/',include('shop_detail.urls')),

]
