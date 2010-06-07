from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^jamfu_facebook/', include('jamfu_facebook.urls')),
    (r'^/', include('socialregistration.urls')),
    (r'^artists/', include('artists.urls')),
)