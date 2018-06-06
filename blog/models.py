from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class zhuce(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class artice(models.Model):  # python

    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    zhaiyao = models.CharField(max_length=300)
    # content = models.TextField(max_length=10000)#非富文本编辑器
    content = RichTextField()  # 富文本编辑器


class UserMssge(models.Model):  # 用户留言
    pro  = models.ForeignKey('artice',to_field='id',on_delete=True,default='')
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=100)


class artice_dj(models.Model):  # django
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    zhaiyao = models.CharField(max_length=300)
    # content = models.TextField(max_length=10000)#非富文本编辑器
    content = RichTextField()  # 富文本编辑器


class artice_ja(models.Model):  # java
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    zhaiyao = models.CharField(max_length=300)
    # content = models.TextField(max_length=10000)#非富文本编辑器
    content = RichTextField()  # 富文本编辑器


class artice_js(models.Model):  # js
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    zhaiyao = models.CharField(max_length=300)
    # content = models.TextField(max_length=10000)#非富文本编辑器
    content = RichTextField()  # 富文本编辑器

class province(models.Model):
    name = models.CharField(max_length=90)

class city(models.Model):
    name = models.CharField(max_length=55)
    pro = models.ForeignKey('province',to_field='id',on_delete=True,default='')