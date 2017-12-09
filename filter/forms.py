from django import forms
from .models import User, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dob', 'gender', 'city', 'description', 'ocupation',
            'monthly_budget', 'tidyness_lvl', 'guests_lvl', 'temperament',
            'is_smoker', 'has_pets', 'is_visible', 'image')
