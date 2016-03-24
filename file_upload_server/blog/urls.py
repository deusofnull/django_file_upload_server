from django.conf.urls import url
from file_upload_server.blog.views import blog_main

urlpatterns = [
    url(r'^$', blog_main, name='blog_main'),
    url(r'^([0-9]{5})/$', list, name='blog_detail')
]
