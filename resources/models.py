from django.db import models
from django.db.models.signals import pre_save

from blogs.models import Category, get_filename_ext
from hexanovate.utils import unique_slug_generator


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=name, ext=ext)
    return "resources/thumbnails/{final_filename}".format(
        new_filename=name,
        final_filename=final_filename
    )


def upload_resource_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=name, ext=ext)
    return "resources/attachments/{final_filename}".format(
        new_filename=name,
        final_filename=final_filename
    )


class Resource(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True, max_length=128)
    thumbnail = models.ImageField(upload_to=upload_image_path)
    category = models.ForeignKey(Category, blank=True, null=True, related_name='resources', on_delete=models.CASCADE)
    author = models.CharField(max_length=128)
    short_description = models.TextField()
    attachment = models.FileField(upload_to=upload_resource_path, blank=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Resource)
