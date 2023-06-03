from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class MyUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "username", "first_name", "last_name", "is_staff"]


# from MyUser, register same fields into MyUserAdmin!
admin.site.register(User, MyUserAdmin)
