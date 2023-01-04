from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('image',)}),
    )

admin.site.register(User, MyUserAdmin)

