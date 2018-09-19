import xadmin
from django.conf.urls import url,include
from shop_detail import views


urlpatterns = [
    url('detial/(\w+)/',views.detial,name='detial'),


]
