from django.conf import settings
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
admin.autodiscover()

import views
from recipes import views as recipes_views
from menus import views as menus_views

urlpatterns = patterns('',
    url(r'^$', views.home.as_view(), name='home'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^recipes/$', recipes_views.RecipeList.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/$', recipes_views.RecipeDetail.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/steps$', recipes_views.StepList.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/steps/(?P<step_order>[0-9]+)$', recipes_views.StepDetail.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/ingredients$', recipes_views.RecipeIngredientList.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)/ingredients/(?P<recipeingredient_pk>[0-9]+)$', recipes_views.RecipeIngredientDetail.as_view()),

    url(r'^menus/$', menus_views.MenuList.as_view()),
    url(r'^menus/(?P<pk>[0-9]+)$', menus_views.MenuDetail.as_view()),
    url(r'^menus/(?P<pk>[0-9]+)/weeks$', menus_views.WeekList.as_view()),
    url(r'^menus/(?P<pk>[0-9]+)/weeks/(?P<week_number>[0-9]+)$', menus_views.WeekDetail.as_view()),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^docs/', include('rest_framework_swagger.urls')),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)

urlpatterns = format_suffix_patterns(urlpatterns)
