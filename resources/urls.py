from django.conf.urls import url

from resources.views import ResourceListView

app_name = 'blogs'

urlpatterns = [
    url(r'^$', ResourceListView.as_view(), name='blog-list'),
]
