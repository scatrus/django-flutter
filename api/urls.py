from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

from django.urls import path
from .views import UserRecordView, UserCreateApiView, UserList

app_name = 'api'

urlpatterns = [
    # url(r'^user/$', UserList),
    url('user/', UserCreateApiView.as_view(), name='users'),

    url(r'^teacher/(?P<pk>[0-9]+)/$', views.teacher_detail),
    url(r'^teacher/$', views.teacher_list),

    url(r'^student/(?P<pk>[0-9]+)/$', views.student_detail),
    url(r'^student/$', views.student_list),

    url(r'^academy/(?P<pk>[0-9]+)/$', views.academy_detail),
    url(r'^academy/$', views.academy_list),

    url(r'^place/(?P<pk>[0-9]+)/$', views.place_detail),
    url(r'^place/$', views.place_list),

    url(r'^classroom/(?P<pk>[0-9]+)/$', views.classroom_detail),
    url(r'^classroom/$', views.classroom_list),

    url(r'^group/(?P<pk>[0-9]+)/$', views.group_detail),
    url(r'^group/$', views.group_list),

    url(r'^presence/(?P<pk>[0-9]+)/$', views.presence_detail),
    url(r'^presence/$', views.presence_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
