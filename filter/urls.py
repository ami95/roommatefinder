from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.profile_list, name='profile_list'),
    url(r'^myprofile$', views.my_profile, name='myprofile'),
    url(r'^updateprofile$', views.update_profile, name='updateprofile'),
        ]
