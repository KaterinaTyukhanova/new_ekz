from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", 'email', )


@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_display = ("name", "date")


@admin.register(Zakaz)
class ZakazAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
