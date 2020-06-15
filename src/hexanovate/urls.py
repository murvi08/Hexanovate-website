from django.conf.urls import url

from hexanovate.views import ContactMessagePostView, SubscribeView, QuestionPostView

app_name = 'hexanovate'

urlpatterns = [
    url(r'^question/post/$', QuestionPostView.as_view(), name='post-question'),
    url(r'^contact-us/post/$', ContactMessagePostView.as_view(), name='post-contact-message'),
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe')
]
