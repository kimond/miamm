from django.conf import settings
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from . import views
from recipes import views as recipes_views

urlpatterns = patterns('',
    url(r'^$', views.home.as_view(), name='home'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^recipes/$', recipes_views.RecipeList.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/$', recipes_views.RecipeDetail.as_view()),

    url(r'^menus/',include('menus.urls', namespace='menus')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)

urlpatterns = format_suffix_patterns(urlpatterns)
