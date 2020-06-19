from django.contrib import admin

from hexanovate.actions import export_as_csv_action
from hexanovate.models import ContactMessage, Subscriber, Question


class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

    list_display = ['first_name', 'last_name', 'guidance', 'phone']
    list_filter = ['guidance', 'timestamp']
    search_fields = ['first_name', 'last_name', 'guidance']


admin.site.register(Question, QuestionAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactMessage

    list_display = ['name', 'subject', 'message']
    list_filter = ['timestamp']
    search_fields = ['name', 'email', 'subject']

    actions = [export_as_csv_action("CSV Export", fields=['timestamp', 'name', 'email', 'subject', 'message'])]


admin.site.register(ContactMessage, ContactMessageAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']

    actions = [export_as_csv_action("CSV Export", fields=['email'])]


admin.site.register(Subscriber, SubscriberAdmin)
