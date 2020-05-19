from django.contrib import admin

# Register your models here.

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_full_name')
    fields = (('is_active', 'is_staff'), 'username', ('first_name', 'last_name'),
        'email', 'date_joined')


admin.site.register(User, UserAdmin)
