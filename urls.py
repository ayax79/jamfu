from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   (r'^', include('socialregistration.urls')),
   (r'^$', 'main.views.index'),
   (r'^login', 'main.views.login'),
   (r'^login_submit', 'main.views.login_submit'),
   (r'^admin/', include(admin.site.urls)),
   (r'^jamfu_facebook/', include('jamfu_facebook.urls')),
   (r'^artists/', include('artists.urls')),
)