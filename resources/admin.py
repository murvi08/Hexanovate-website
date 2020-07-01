from django.contrib import admin

from resources.models import Resource


class ResourceAdmin(admin.ModelAdmin):
    class Meta:
        model = Resource

    list_display = ['title', 'category', 'author', 'timestamp']
    list_filter = ['category', 'timestamp', 'active']
    search_fields = ['title', 'author', 'category']
    fieldsets = (
        ('Resource Details', {'fields': ('title', ('author', 'slug'), ('category', 'thumbnail'))}),
        ('Resource Content', {'fields': ('short_description', 'attachment')})
    )


admin.site.register(Resource, ResourceAdmin)
