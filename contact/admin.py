from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'message')
    list_display_links = ('firstname', 'lastname', 'email', 'message')
    list_filter = ('firstname', 'lastname', 'email')
    search_fields = ['email', 'message']
