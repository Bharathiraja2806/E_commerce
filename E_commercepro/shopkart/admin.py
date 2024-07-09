from django.contrib import admin
from .models import *


class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')

admin.site.register(Product)
admin.site.register(category, categoryAdmin)

