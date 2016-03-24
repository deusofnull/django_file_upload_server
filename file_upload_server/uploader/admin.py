from django.contrib import admin

from file_upload_server.uploader.models import Document
admin.site.register(Document)

from file_upload_server.blog.models import Blog, Comment
admin.site.register(Blog)
admin.site.register(Comment)
