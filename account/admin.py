import xadmin
from account.models import *
from xadmin import views


# Register your models here.
# 全局配置
from xadmin import views
# 开启主题修改
class BaseStyleSettings:
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)

class GlobalSettings:
    site_title = 'xx后台管理系统'
    site_footer = 'xxx科技有限公司'
    menu_style = 'accordion'  # 后台菜单样式修改
xadmin.site.register(views.CommAdminView, GlobalSettings)

class ShopAdmin:
    list_display=['shop_id','name','original_price','promote_price','sub_title']
    #多字段搜索
    search_fields=['name','sub_title']
    #分页 的条数
    list_per_page=10

xadmin.site.register(Shop,ShopAdmin)