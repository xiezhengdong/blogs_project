from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class zhuce(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class artice(models.Model):#python
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    zhaiyao = models.CharField(max_length=300)
    #content = models.TextField(max_length=10000)#非富文本编辑器
    content = RichTextField()#富文本编辑器

class artice_dj(models.Model):#django
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    content = models.CharField(max_length=100000)

class artice_ja(models.Model):#java
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    content = models.CharField(max_length=100000)

class artice_js(models.Model):#js
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    content = models.CharField(max_length=100000)
