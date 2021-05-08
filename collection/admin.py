from django.contrib import admin
from .models import Carpet

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ('image_tag', 'price', 'width', 'height', 'fineness', 'origin', 'style', 'material', 'sold',)

readonly_fields = ('image_tag',)

admin.site.register(Carpet, ProductAdmin)