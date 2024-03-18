from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import CustomUser

class UserAdmin(ModelAdmin):
   model = CustomUser
   search_fields = ['email']

admin.site.register(CustomUser,UserAdmin)