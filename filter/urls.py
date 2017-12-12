from django.conf.urls import url
from . import views
from django_filters.views import FilterView
from .filters import UserFilter

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^myprofile$', views.my_profile, name='myprofile'),
    url(r'^updateprofile$', views.update_profile, name='updateprofile'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^home$', views.render_home, name='render_home'),

        ]
