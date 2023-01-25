from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^student$', views.student_list),
    re_path(r'^student/(?P<pk>[0-9]+)/$', views.student_detail),
    re_path(r'^subject$', views.subject_list),
    re_path(r'^subject/(?P<pk>[0-9]+)/$', views.subject_detail),
    re_path(r'^fraction$', views.fraction_list),
    re_path(r'^fraction/(?P<pk>[0-9]+)/$', views.fraction_detail),
    # re_path(r'^student/score$', views.student_score_list),
    # re_path(r'^student/score/(?P<pk>[0-9]+)/$', views.student_score_detail),
]
