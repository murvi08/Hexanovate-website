from django.conf.urls import url

from resources.views import ResourceListView

app_name = 'resources'

urlpatterns = [
    url(r'^$', ResourceListView.as_view(), name='resource-list'),
]
