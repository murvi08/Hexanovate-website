from django.conf.urls import url

from hexanovate.views import ContactMessagePostView, SubscribeView

app_name = 'hexanovate'

urlpatterns = [
    url(r'^contact-us/post/$', ContactMessagePostView.as_view(), name='post-contact-message'),
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe')
]
