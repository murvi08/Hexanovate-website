from django.views.generic import ListView

from blogs.models import Category, Blog
from resources.models import Resource


class ResourceListView(ListView):
    queryset = Resource.objects.filter(active=True)
    template_name = "resources.html"

    def get_queryset(self):
        filter_category = self.request.GET.get('category')
        if filter_category is not None:
            return self.queryset.filter(category__id=filter_category)
        return self.queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ResourceListView, self).get_context_data()
        context['resources'] = self.get_queryset().order_by('-timestamp')

        blogs = Blog.objects.filter(active=True)
        context['blogs'] = blogs.order_by('-date')
        context['categories'] = Category.objects.all()
        context['recent_blogs'] = blogs.order_by('-date')[:2]

        filter_category = self.request.GET.get('category')
        if filter_category is not None:
            context['selected_category'] = int(filter_category)
        return context
