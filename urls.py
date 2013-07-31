from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tools2.views.home', name='home'),
    # url(r'^django_tools2/', include('django_tools2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


    (r'^$', views.search,
         { 'template_name' :'index.html'}),
    (r'^search$', views.search,
         { 'template_name' :'search_ansd.html'}),
    (r'^group_search$', views.group_seach,
         { 'template_name' :'group_search_ansd.html'})

)
