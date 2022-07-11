from django.contrib import admin
from shorturl.models import Urls


# Register your models here.
@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ("url", "short",)
    fields = ("url", "short", "created_at",)
    search_fields = ("short", "url",)
