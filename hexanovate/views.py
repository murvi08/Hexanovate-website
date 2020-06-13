from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from hexanovate.models import ContactMessage, Subscriber


class ContactMessagePostView(CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'subject', 'message']
    template_name = "contact-us.html"

    def post(self, request, *args, **kwargs):
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        messages.success(request, "Thank you for contacting us! We will reach out to you soon!")
        return HttpResponseRedirect(reverse('contact-us'))


class SubscribeView(CreateView):
    model = Subscriber
    fields = ['email']

    def post(self, request, *args, **kwargs):
        instance, created = Subscriber.objects.get_or_create(email=request.POST.get('email'))
        if created:
            messages.success(request, "Your subscription is added successfully!")
        else:
            messages.warning(request, "You are already subscribed to Hexanovate")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
