from django.contrib import admin
from django.db import models
from .models import Trabajos, CategoriaTrab
# Register your models here.

class TrabajosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoriaTrabAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Trabajos, TrabajosAdmin)
admin.site.register(CategoriaTrab, CategoriaTrabAdmin)