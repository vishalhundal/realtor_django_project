from django.contrib import admin

# Register your models here.
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")

admin.site.register(Realtor, RealtorAdmin)