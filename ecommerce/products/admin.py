from django.contrib import admin
from .models import Customer,Products
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
	list_display=['id','c_name']
admin.site.register(Customer,CustomerAdmin)

class ProductsAdmin(admin.ModelAdmin):
	list_display=['id','p_name','c_id']

admin.site.register(Products,ProductsAdmin)
