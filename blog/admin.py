from django.contrib import admin
from blog.models import zhuce,artice

# Register your models here.

admin.site.site_header = '博客管理后台'
admin.site.register(zhuce)
admin.site.register(artice)