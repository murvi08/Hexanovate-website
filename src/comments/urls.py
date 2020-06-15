from django.conf.urls import url

from comments.views import PostCommentView

app_name = 'comments'

urlpatterns = [
    url(r'^add/(?P<blog_id>[0-9a-z+]+)/$', PostCommentView.as_view(), name='post-comment')
]