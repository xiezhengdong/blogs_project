from django.db import models

# Create your models here.

class zhuce(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class artice(models.Model):#python
    title = models.CharField(max_length=100)
    shjian = models.CharField(max_length=50)
    content = models.CharField(max_length=100000)

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
