from django.contrib import admin
from .models import Xomashyo, XomashyoMahsulot, Mahsulot, Store
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ["xomashyo_id", "price", "remainder"]


class XomashyoAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MahsulotAdmin(admin.ModelAdmin):
    list_display = ["name", "kodi"]


class XomashyoMahsulotAdmin(admin.ModelAdmin):
    list_display = ["mahsulot_id", "xomashyo_id", "quantity"]


admin.site.register(Mahsulot, MahsulotAdmin)
admin.site.register(Xomashyo, XomashyoAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(XomashyoMahsulot, XomashyoMahsulotAdmin)