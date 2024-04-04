from django.contrib import admin

from projectApp.models import Contact


@admin.register(Contact)
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    pass
