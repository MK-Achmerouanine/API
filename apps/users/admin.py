from django.contrib import admin
from .models import Author
from django.utils.html import format_html
admin.site.site_title = "Super Blog"
admin.site.site_header = format_html(f'<img src="/static/logo.png" height="50" width="120"/> Welcome to Super BLog')
# admin.site.site_url = "Barbaros"

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    '''Admin View for Author'''

    list_display = ('name','user')
    list_filter = ('user',)
    inlines = [
        # Inline,
    ]
    # raw_id_fields = ('',)
    readonly_fields = ('created_at',)
    search_fields = ('name',)
    # date_hierarchy = ''
    ordering = ('-name',)