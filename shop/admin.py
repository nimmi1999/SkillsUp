from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Blog

admin.site.register(Product)

admin.site.register(Contact)

admin.site.register(Blog)
