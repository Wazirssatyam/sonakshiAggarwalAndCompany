from django.contrib import admin
from sonakshi.models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.register(MyUser)
UserAdmin.fieldsets +=("Custom",{'fields':('mobile_number','birth_date')}),