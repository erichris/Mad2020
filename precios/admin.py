from django.contrib import admin

from precios.models import ModulesPrice, Textures
# Register your models here.


class ModulePriceAdmin(admin.ModelAdmin):
    list_display = ("typeOf", "size", "door", "interiorBlanco", "price")


class TexturesAdmin(admin.ModelAdmin):
    list_display = ("name", "img")


admin.site.register(ModulesPrice, ModulePriceAdmin)
admin.site.register(Textures, TexturesAdmin)
