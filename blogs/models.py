import os
import random

from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from hexanovate_website.utils import unique_slug_generator


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True)
    thumbnail = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, related_name='blogs', on_delete=models.CASCADE)
    author = models.CharField(max_length=128)
    short_description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends')
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)
    related_blogs = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='related_blogs_reverse')
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blogs:" + "blog-detail", kwargs={"slug": self.slug})

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


pre_save.connect(product_pre_save_receiver, sender=Blog)


