from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search$', views.search, name='search'),
    url(r'^myprofile$', views.my_profile, name='myprofile'),
    url(r'^updateprofile$', views.update_profile, name='updateprofile'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^$', views.render_home, name='render_home'),
        ]
