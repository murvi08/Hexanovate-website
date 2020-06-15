from django.views.generic import TemplateView

from blogs.models import Blog

blog_queryset = Blog.objects.filter(active=True)


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blogs'] = blog_queryset.order_by("-date")
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data()
        context['blogs'] = blog_queryset.order_by("-date")
        return context


class PortfolioPageView(TemplateView):
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        context = super(PortfolioPageView, self).get_context_data()
        context['blogs'] = blog_queryset.order_by("-date")
        return context


class GalleryPageView(TemplateView):
    template_name = "gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryPageView, self).get_context_data()
        context['blogs'] = blog_queryset.order_by("-date")
        return context


class ContactUsPageView(TemplateView):
    template_name = "contact-us.html"

    def get_context_data(self, **kwargs):
        context = super(ContactUsPageView, self).get_context_data()
        context['blogs'] = blog_queryset.order_by("-date")
        return context
