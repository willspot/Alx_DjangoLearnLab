from django.contrib import admin

# bookshelf/admin.py
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register the Book model to manage it via Django admin
admin.site.register(Book)

# Add custom group and permissions setup
def create_groups_and_permissions():
    # Ensure necessary permissions are created for the 'Book' model
    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    # Create Groups
    editor_group, created = Group.objects.get_or_create(name='Editors')
    editor_group.permissions.add(can_create, can_edit)
    
    viewer_group, created = Group.objects.get_or_create(name='Viewers')
    viewer_group.permissions.add(can_view)
    
    admin_group, created = Group.objects.get_or_create(name='Admins')
    admin_group.permissions.add(can_view, can_create, can_edit, can_delete)

# Call this function after migration or once when your app starts
create_groups_and_permissions()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

# Create a custom admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters in the admin interface
    list_filter = ('author', 'publication_year')

    # Enable search functionality on title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the customized admin interface
admin.site.register(Book, BookAdmin)


# Register your models here.
