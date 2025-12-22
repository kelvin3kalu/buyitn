from django.contrib import admin
from .models import Product, Order,Category
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.site_header = "BuyItn Admin"
admin.site.site_title = "BuyItn Admin Portal"
admin.site.index_title = "Welcome to BuyItn Admin Portal"
