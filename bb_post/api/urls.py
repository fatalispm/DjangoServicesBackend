from django.conf.urls import patterns, url

from .views import token
from .views import post
from .views import comment

urlpatterns = patterns('',
    url(r'^$', post.Collection.as_view()),
    url(r'^/(?P<post_id>\d+)$', post.Single.as_view()),
    url(r'^/token$', token.GetTokenView.as_view(), name='get-token'),
    url(r'^/comment$', comment.Collection.as_view())
)
