from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^api/', include(patterns('',
        url(r'^posts', include('bb_post.api.urls')),
    ))),
    url(settings.ADMIN_URL, admin.site.urls),
)
