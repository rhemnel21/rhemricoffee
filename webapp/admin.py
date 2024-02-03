from django.contrib import admin
from .models import CustomersInfo, Product, Order, OrderDetail, Transaction

# Register your models here.

admin.site.register(CustomersInfo)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Transaction)