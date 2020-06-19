from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blogs.models import Blog, Category


class BlogListView(ListView):
    queryset = Blog.objects.filter(active=True)
    template_name = "blogs.html"

    def get_queryset(self):
        filter_category = self.request.GET.get('category')
        if filter_category is not None:
            return self.queryset.filter(category__id=filter_category)
        return self.queryset

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data()
        context['blogs'] = self.get_queryset().order_by('-date')
        context['categories'] = Category.objects.all()
        context['recent_blogs'] = self.queryset.order_by('-date')[:2]

        filter_category = self.request.GET.get('category')
        if filter_category is not None:
            context['selected_category'] = int(filter_category)
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
        context['recent_blogs'] = self.queryset.order_by('-date')[:2]
        context['categories'] = Category.objects.annotate(blogs_count=Count('blogs')).order_by('-blogs_count')[:5]
        return context
