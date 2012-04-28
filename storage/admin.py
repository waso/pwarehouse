from models import Category, Item, Storage, Currency, TaxRate, ItemsBucket, Document
from django.contrib import admin

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemsBucket)
admin.site.register(Storage)
admin.site.register(Currency)
admin.site.register(TaxRate)
admin.site.register(Document)