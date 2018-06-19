from django.contrib import admin
from .models import Deal, Category, Vendor

admin.site.register(Vendor)
admin.site.register(Deal)
admin.site.register(Category)
