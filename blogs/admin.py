from django.contrib import admin

from blogs.models import Category, Tag, Blog

admin.site.register(Category)
admin.site.register(Tag)


class RelatedBlogsInline(admin.TabularInline):
    model = Blog.related_blogs.through
    extra = 0
    fk_name = 'from_blog'
    verbose_name = "Related Blog"
    verbose_name_plural = "Related Blogs"


class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog

    inlines = [RelatedBlogsInline]
    list_display = ['title', 'category', 'author', 'date']
    list_filter = ['category', 'date', 'active']
    search_fields = ['title', 'author', 'category', 'tags']
    filter_horizontal = ['tags']
    fieldsets = (
        ('Blog Details', {'fields': ('title', ('author', 'slug'), ('category', 'thumbnail'), 'tags',)}),
        ('Blog Content', {'fields': ('short_description', 'content')})
    )


admin.site.register(Blog, BlogAdmin)
