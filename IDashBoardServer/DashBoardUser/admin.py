from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from DashBoardUser.models import DashBoardUser
# Register your models here.

class DashBoardUserInline(admin.StackedInline):
    model = DashBoardUser
    can_delete = False
    verbose_name_plural = 'dashboarduser'

class UserAdmin(UserAdmin):
    inlines = (DashBoardUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
