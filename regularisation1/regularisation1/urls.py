from django.conf.urls import patterns, include, url
from input.views import regularization, change, show_original
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'regularisation1.views.home', name='home'),
    # url(r'^regularisation1/', include('regularisation1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^regularization/$', regularization),
    url(r'^regularization/change/(?P<pos>\d)/$', change, name='change'),
    url(r'^regularization/show/$', show_original), 
)

# if settings.DEBUG:
#     urlpatterns += patterns('',
#                             #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media'}),
#         (r'', include('staticfiles.urls')),
#     )
