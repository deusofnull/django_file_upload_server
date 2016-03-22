from django.conf.urls import url
from file_upload_server.uploader.views import list

urlpatterns = [
    url(r'^list/$', list, name='list')
]
