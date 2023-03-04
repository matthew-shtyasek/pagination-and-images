from django.contrib import admin

from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date']
    readonly_fields = ['create_date']
    search_fields = ['title']
    list_filter = ['create_date']
    fields = ['title', 'image', 'create_date']
