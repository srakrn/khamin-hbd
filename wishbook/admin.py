from django.contrib import admin
from .models import Wish

# Register your models here.


class WishAdmin(admin.ModelAdmin):
    list_display = ("id", "wish_text", "wish_owner")
    readonly_fields = ("created", )


admin.site.register(Wish, WishAdmin)
