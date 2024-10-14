from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','user_type','is_active']

    def username(self,obj):
        return obj.user.username

    def first_name(self,obj):
        return obj.user.first_name

    def last_name(self,obj):
        return obj.user.last_name

    def user_type(self,obj):
        return obj.user.user_type

    def is_active(self,obj):
        return obj.user.is_active

admin.site.register(CustomUser,CustomUserAdmin)