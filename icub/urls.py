from django.conf.urls.defaults import *

try:
    from local_urls import urlpatterns
except Exception, e:
    print e
    urlpatterns = patterns('', (r'^$', 'home.views.index'),)

urlpatterns += patterns('',
    # Example:
    # (r'^icub/', include('icub.foo.urls')),
    (r'^$', 'home.views.index'),

    # Uncomment this for admin:
     (r'^admin/', include('django.contrib.admin.urls')),
)
