from django.contrib import admin

from hexanovate.models import ContactMessage, Subscriber


class ContactMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactMessage

    list_display = ['name', 'subject', 'message']
    list_filter = ['timestamp']
    search_fields = ['name', 'email', 'subject']


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Subscriber)
