from django.conf.urls.defaults import patterns

urlpatterns = patterns('jamfu_facebook.views',
    (r'^$', 'index'),
)