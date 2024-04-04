from django.contrib import admin

from blogApp.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "-empty-"
    list_display = (
        "title",
        "counted_views",
        "status",
        "published_date",
    )
    list_filter = ("status",)
    ordering = ["created_date"]
    search_fields = ("title",)

    # در صفحه دستکاری و ادیت فیلدهای پست به ورودی های زیر دسترسی داریم
    # fields = ("title",)


# admin.site.register(Post)
