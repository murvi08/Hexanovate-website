from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from hexanovate_website.views import (
    HomePageView, AboutPageView, PortfolioPageView,
    GalleryPageView, ContactUsPageView
)

urlpatterns = [
    path('google-auth/', TemplateView.as_view(template_name="google-auth.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^about/$', AboutPageView.as_view(), name='about'),
    url(r'^portfolio/$', PortfolioPageView.as_view(), name='portfolio'),
    url(r'^gallery/$', GalleryPageView.as_view(), name='gallery'),
    url(r'^contact-us/$', ContactUsPageView.as_view(), name='contact-us'),

    url(r'^/', include("hexanovate.urls", namespace='hexanovate')),
    url(r'^blogs/', include("blogs.urls", namespace='blogs')),

    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

admin.site.site_header = "Hexanovate Administration"
admin.site.site_title = "Hexanovate Admin Portal"
admin.site.index_title = "Welcome to Hexanovate Admin Portal"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
