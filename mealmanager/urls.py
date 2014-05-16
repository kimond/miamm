from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home.as_view(), name='home'),

    url(r'^recipemanager/', include('recipemanager.urls', namespace="recipemanager")),

    url(r'^menu/',include('menumaker.urls', namespace='menu')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
