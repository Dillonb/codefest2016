from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'eventsapp.views.home_view'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'eventsapp/login.html'}),
    url(r'^accounts/logout/$', 'eventsapp.views.logout_view'),
    url(r'^accounts/profile/$', 'eventsapp.views.profile_view'),

    url(r'^calendar$', 'eventsapp.views.calendar_view'),
    url(r'^calendar/list', 'eventsapp.views.calendar_list_view'),
    url(r'^calendar/submit', 'eventsapp.views.submit_event_view'),
    url(r'^calendar/day$', 'eventsapp.views.day_view'),
    url(r'^calendar/week$', 'eventsapp.views.week_view'),

    url(r'^clubs/(?P<clubid>\d+)$', 'eventsapp.views.club_view'),
    url(r'^clubs/list', 'eventsapp.views.club_list_view'),
    url(r'^clubs/submit', 'eventsapp.views.club_submit_view'),

	url(r'^tests$','eventsapp.views.tests_view'),
)
