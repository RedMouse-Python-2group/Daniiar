from django.contrib import admin

# Register your models here.
from .models import Author


class UsersModelAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "register_date", ]
    list_filter = ["register_date"]
    search_fields = ["first_name", "last_name"]
    class Meta:
        model = Author
admin.site.register(Author, UsersModelAdmin)