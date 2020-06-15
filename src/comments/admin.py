from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment

    list_display = ['name', 'blog', 'message']
    list_filter = ['timestamp']
    search_fields = ['name', 'email', 'blog.title']


admin.site.register(Comment, CommentAdmin)
