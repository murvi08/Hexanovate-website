import random
import string

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.text import slugify

from hexanovate_website.settings import EMAIL_HOST_USER


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance):
    order_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def send_subscription_email(recipient_email):
    subject = "Thank You From Hexanovate!"
    message = "Thank You for subscribing to Hexanovate! Please stay tuned for exciting posts and updates!"
    sender_email = EMAIL_HOST_USER

    send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)


def send_get_in_touch_email_to_user(recipient_email):
    subject = "Thank You From Hexanovate for contacting us!"
    message = "Thank you for reaching out to us. We have received your message! We will get back to you soon!"
    sender_email = EMAIL_HOST_USER

    send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)


def send_get_in_touch_email_to_host(contact_message):
    subject = "Hexanovate: New Message Received!"
    html_message = render_to_string("get-in-touch-mail.html", {'contact_message': contact_message})
    sender_email = EMAIL_HOST_USER

    send_mail(subject, None, sender_email, [EMAIL_HOST_USER], fail_silently=False, html_message=html_message)

