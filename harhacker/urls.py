from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^login$',  'django.contrib.auth.views.login', {'template_name': 'login.html'}, 'login'),
    (r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, 'logout'),
    (r'^$', 'harhacker.dashboards.views.home', {}, 'home'),
    (r'^pollers', include('harhacker.pollers.urls', namespace='pollers')),
)
