from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from blogs.models import Blog
from comments.models import Comment


class PostCommentView(CreateView):
    model = Comment
    fields = ['name', 'email', 'message']
    template_name = 'blog-detail.html'

    def post(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs.get('blog_id'))
        comment = Comment.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
            blog=blog
        )
        messages.success(request, "Your comment has been added!")
        return HttpResponseRedirect(reverse('blogs:blog-detail', args=[blog.slug]))
