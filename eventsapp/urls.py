from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'eventsapp/home.html'}),
    url(r'^accounts/logout/$', 'eventsapp.views.logout_view'),
    url(r'^$', 'eventsapp.views.home_view'),
    url(r'^calendar$', 'eventsapp.views.calendar_view')
)
