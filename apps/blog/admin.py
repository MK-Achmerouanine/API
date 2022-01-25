from django.contrib import admin
from .models import Post
# admin.site.site_url = "Barbaros"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title','created_by')
    list_filter = ('created_by',)
    inlines = [
        # Inline,
    ]
    # raw_id_fields = ('',)
    readonly_fields = ('created_at',)
    search_fields = ('title',)
    # date_hierarchy = ''
    ordering = ('-created_at',)