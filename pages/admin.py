from django.contrib import admin

from pages.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title',
              'text',
              'published',
              'author',
              'create_date',
              'edit_date']
    readonly_fields = ['create_date',
                       'edit_date']
    search_fields = ['title',
                     'text']
    list_filter = ['create_date',
                   'edit_date',
                   'published']
    list_display = ['title',
                    'published',
                    'author',
                    'create_date',
                    'edit_date']
    list_editable = ['published']