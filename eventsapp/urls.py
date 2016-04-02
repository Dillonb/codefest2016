from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'eventsapp/login.html'}),
    url(r'^accounts/logout/$', 'eventsapp.views.logout_view'),
    url(r'^$', 'eventsapp.views.home_view')
)
