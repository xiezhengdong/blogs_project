# -*- coding:utf-8 -*-
from django.conf.urls import url
from blog import views

blog_obj = views.BlogAlls()
urlpatterns = [
    url('^login/$', blog_obj.login, name='login'),
    url('^register/$', blog_obj.register, name='register'),
    url('^index/$', blog_obj.index),
    url('^cook_login/$', blog_obj.cook_login),
    url('^cook_index/$', blog_obj.cook_index),
    url('^liuyan/$', blog_obj.liuyan),
    # url('^python/$',blog_obj.python),
    # url('^django/$',blog_obj.django),
    url('^python/page/$', blog_obj.page_py),
    url('^django/page/$', blog_obj.page_dj),
    url('^text_html/$', blog_obj.test_html),
    url('^python/content/(\d+)$', blog_obj.content),
    url('^upload/$', blog_obj.upload),
    url('^download/file/$', blog_obj.download),
    url('^data/$', blog_obj.display_data),
    url('^user/message/$', blog_obj.user_message),
    url('^about/$', blog_obj.about_author)


]
