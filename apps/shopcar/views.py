from django.shortcuts import render

# Create your views here.
from account.models import ShopCar


def add(request):

    uid=request.user.id
    shop_id=request.GET.get('shop_id')
    number=request.GET.get('number')
    """
       当商品存在购物车,更新数量
       不存在, 创纪录

       """
    car=ShopCar.objects.filter(uid=uid,shop_id=shop_id)
    if car:
        #存在购物车,更新
        car.number.F('number')+number
        # car.number+=number
        car.save(update_fields=['number'])
    else:
        car=ShopCar(uid=uid)

def delete(request):
    pass
def update(request):
    pass

def find(fequest):
    pass