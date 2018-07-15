from django.contrib import admin
from app.check.models import Check, Item, Category


admin.site.register(Check)
admin.site.register(Item)
admin.site.register(Category)