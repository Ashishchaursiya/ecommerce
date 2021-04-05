from django.contrib import admin
from .models import Banner,Product,ProductImage,Order,updateOrder
# Register your models here.
admin.site.register(Banner)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(updateOrder)
