from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('harhacker.pollers.views',
    url(r'^$', 'index', name='index'),
)
