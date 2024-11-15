from django.contrib import admin
from .models import Owner

@admin.register(Owner)
class CustomOwnerAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','user_type']

    def username(self,obj):
        return obj.user.username
    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name
    def user_type(self,obj):
        return obj.user.user_type
