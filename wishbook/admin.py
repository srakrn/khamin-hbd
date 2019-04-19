from django.contrib import admin
from .models import Wish

# Register your models here.


class WishAdmin(admin.ModelAdmin):
    list_display = ("wish_text", "wish_owner")


admin.site.register(Wish, WishAdmin)
