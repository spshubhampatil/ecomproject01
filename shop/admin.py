from django.contrib import admin
from shop.models.product import Product,ProductImage 
from shop.models.user import User
from shop.models.payment import Payment

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(User)
admin.site.register(Payment)