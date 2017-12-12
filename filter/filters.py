from .models import User, Profile
from django import forms
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]

class ProfileFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    monthly_budget = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    monthly_budget__gt = django_filters.NumberFilter(name='monthly_budget', lookup_expr='monthly_budget__gt')
    monthly_budget__lt = django_filters.NumberFilter(name='monthly_budget', lookup_expr='monthly_budget__lt')
    class Meta:
        model = Profile
        fields = ['dob', 'gender', 'city', 'description', 'ocupation',
            'monthly_budget', 'tidyness_lvl', 'guests_lvl', 'temperament',
            'is_smoker', 'has_pets', 'is_visible',]
