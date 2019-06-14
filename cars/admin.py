# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Car,Person

# Register your models here.
admin.site.register(Car)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['name','address','drivers_license','slug']
    list_editable = ['name','address','drivers_license']
    prepopulated_fields = {'slug': ('name',)}
locals()