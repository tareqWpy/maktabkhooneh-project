from django.contrib import admin

from projectApp.models import Contact


@admin.register(Contact)
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ("name", "email", "created_date")
    list_filter = ("email",)
    search_fields = ("name", "message")

    class Meta:
        ordering = ["email"]
