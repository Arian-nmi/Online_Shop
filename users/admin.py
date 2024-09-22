from django.contrib import admin
from .models import User
<<<<<<< HEAD


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)
    search_fields = ('username',)


admin.site.register(User, UserAdmin)
=======


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = 'username'


admin.site.register(User, UserAdmin)


>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2
