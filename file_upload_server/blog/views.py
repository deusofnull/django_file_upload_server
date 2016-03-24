from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse

from file_upload_server.blog.models import Blog, Comment
from .forms import BlogForm

def blog_main(request):

    if request.method == 'POST':
        # create form instance and populate it with data from request
        blog_form = BlogForm(request.POST) # blog_form is now a ~bound form~
        if blog_form.is_valid():
            # prcess data in form.cleand_data as required
            '''
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            '''
            author = blog_form.cleaned_data['author']
            title = blog_form.cleaned_data['title']
            text = blog_form.cleaned_data['text']

            new_blog = Blog(author=author, title=title, text=text)
            new_blog.save()
            # redirect to new URL:
            return HttpResponseRedirect('/blog/')
    elif request.method == 'GET':
        # get 5 blogs
        blogs = Blog.objects.all()[:5]

        for blog in blogs:
            comments = blog.comment_set.all()

        # create blank form when http method is GET
        blog_form = BlogForm()

        return render(request,
            'blog/blog.html',
            {'blogs': blogs, 'comments': comments, 'blog_form': blog_form}
        )
    else:
        return HttpResponseNotFound('<h1> Method not supported </h1>')
