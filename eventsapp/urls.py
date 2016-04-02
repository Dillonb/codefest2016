from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'eventsapp/login.html'}),
    url(r'^accounts/logout/$', 'eventsapp.views.logout_view'),
    url(r'^$', 'eventsapp.views.home_view'),
    url(r'^accounts/profile/$', 'eventsapp.views.profile_view'),
    url(r'^calendar/day$', 'eventsapp.views.day_view'),
    url(r'^calendar/week$', 'eventsapp.views.week_view'),
    url(r'^calendar/$', 'eventsapp.views.calendar_view')
    url(r'^calendar$', 'eventsapp.views.calendar_view'),
)
