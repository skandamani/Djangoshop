from django.contrib import admin
from .models import Mobile

class MobileAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'image')
    search_fields = ('brand', 'model')
admin.site.register(Mobile, MobileAdmin)
