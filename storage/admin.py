from models import Category, Item, Storage, Currency, TaxRate, Price, ItemsBucket
from django.contrib import admin

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemsBucket)
admin.site.register(Storage)
admin.site.register(Currency)
admin.site.register(Price)
admin.site.register(TaxRate)