from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.site_header = "Hamro Agro Farm"
admin.site.site_title = "Hamro Agro Farm"
admin.site.index_title = "Welcome Admin"


# Mix profile info and user info
class ProfileInline(admin.StackedInline):
	model = Profile
	exclude = ('old_cart',)
	can_delete=False

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]
	list_display = ('username', 'email', 'first_name', 'last_name','is_active','is_staff','is_superuser')
	search_fields=('email','first_name')
	list_per_page=10
	readonly_fields=('username','email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address',)
    search_fields = ('user', 'phone')
    list_per_page = 10
    exclude = ('old_cart',)


# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)