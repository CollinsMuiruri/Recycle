from django.contrib import admin
from .models import CompanyProfile,Category,Product,Blog
# Register your models here.
admin.site.register(CompanyProfile)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Category)