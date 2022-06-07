from django.db import models
from django.utils.translation import gettext_lazy as _
from newsportal.minixs import TranslateMixin
import os
from datetime import datetime
import random
from django.contrib.auth.models import User

# Create your models here.


def upload_to(name):
    def handle(instance, filename):
        ext = os.path.splitext(filename)[1]

        return "{}/{:%Y-%m}/{:%Y-%m-%d-%H-%M-%S}.{}.{}".format(
            name,
            datetime.now(),
            datetime.now(),
            datetime.now(),
            random.randint(10000, 99999),
            ext
        )

    return handle


def posts_upload_to(instance, filename):
    return upload_to("posts")(instance, filename)


def carousel_upload_to(instance, filename):
    return upload_to("carousel")(instance, filename)


class Carousel(models.Model):
    image = models.ImageField(upload_to=carousel_upload_to)
    header = models.CharField(max_length=50, null=True, default=None)
    comment = models.CharField(max_length=200, null=True, default=None)


class Category(TranslateMixin, models.Model):
    translate_attributes = ['name']
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(TranslateMixin, models.Model):
    translate_attributes = ['subject', 'content']

    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, default=None, null=True)
    subject_uz = models.CharField(max_length=100, verbose_name=_("Sarlavha (uz)"))
    subject_ru = models.CharField(max_length=100, verbose_name=_("Sarlavha (ru)"))
    content_uz = models.TextField(verbose_name=_("Izoh (uz)"))
    content_ru = models.TextField(verbose_name=_("Izoh (ru)"))
    image = models.ImageField(verbose_name=_("img"), upload_to=posts_upload_to)
    read = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
