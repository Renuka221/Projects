from django.contrib import admin
from .models import Customer, ProductPurchase, CustomerMessage, ChurnFeature

admin.site.register(Customer)
admin.site.register(ProductPurchase)
admin.site.register(CustomerMessage)
admin.site.register(ChurnFeature)
