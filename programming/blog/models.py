import re

from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidator, lnglat_validator, ZipCodeValidator
from .fields import PhoneNumberField



class Post(models.Model):
    title = models.CharField(max_length=100,

        validators=[MinLengthValidator(4)],

        verbose_name = '제목')
    content = models.TextField(help_text='Markdown 문법을 써 주세요.',
        validators=[MinLengthValidator(10)])
    tag_set = models.ManyToManyField('Tag', blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'id':self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.CharField(max_length=300)
    author = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'id':self.id})

    # def get_absolute_url(self):
    #     return reverse("blog:post_detail", kwargs={'id':self.id})

class Tag(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_number = PhoneNumberField()
    zip_code = models.CharField(max_length=5, validators=[ZipCodeValidator(True)],verbose_name='신우편번호')

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):

    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline



class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class ZipCode(models.Model):
    city = models.CharField(max_length=20)
    road = models.CharField(max_length=20)
    dong = models.CharField(max_length=20)
    gu = models.CharField(max_length=20)
    code = models.CharField(max_length=7)
