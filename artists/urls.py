from django.conf.urls.defaults import patterns

urlpatterns = patterns('artists.views',
    (r'^$', 'index'),
)