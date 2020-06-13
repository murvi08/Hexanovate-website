from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blogs.models import Blog


class BlogListView(ListView):
    queryset = Blog.objects.filter(active=True)
    template_name = "blogs.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data()
        context['blogs'] = self.queryset.order_by('-date')
        return context


class BlogDetailView(DetailView):
    queryset = Blog.objects.filter(active=True)
    template_name = "blog-detail.html"
    context_object_name = "blog"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Blog, slug=slug, active=True)
        return instance

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data()
        context['blogs'] = self.queryset
        return context
