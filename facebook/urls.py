from django.conf.urls.defaults import patterns

urlpatterns = patterns('jamfu.facebook.views',
    (r'^$', 'index'),
)