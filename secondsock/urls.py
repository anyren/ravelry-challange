from django.conf.urls.defaults import *
from secondsock.views import hello
from secondsock.views import secondsock

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^secondsock/', include('secondsock.foo.urls')),

    ('^$', secondsock),

    ('^hello/$', hello),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
