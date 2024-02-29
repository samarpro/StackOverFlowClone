from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    ordering=('date_joined',)
    list_display=['email','first_name','last_name',]
    fieldsets=()

admin.site.register(models.CustomUser,CustomUserAdmin)
