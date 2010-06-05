from django.conf.urls.defaults import patterns

urlpatterns = patterns('artist.views',
    (r'^$', 'index'),
)