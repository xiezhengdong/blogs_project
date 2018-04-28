from django.contrib import admin
from blog.models import zhuce,artice,artice_dj,artice_ja,artice_js

# Register your models here.

admin.site.site_header = '博客管理后台'
admin.site.register(zhuce)
admin.site.register(artice)
admin.site.register(artice_dj)
admin.site.register(artice_ja)
admin.site.register(artice_js)