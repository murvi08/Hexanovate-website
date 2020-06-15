from django.conf.urls import url, include

from blogs.views import BlogListView, BlogDetailView

app_name = 'blogs'

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='blog-list'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetailView.as_view(), name='blog-detail'),
    url(r'^comments/', include("comments.urls", namespace='comments')),
]
