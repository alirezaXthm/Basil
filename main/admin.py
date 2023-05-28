from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tour


class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'registered','created', 'id', ]


admin.site.register(Tour, TourAdmin)