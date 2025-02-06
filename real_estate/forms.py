from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Property

#CustomUserCreationForm
class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')

#PropertyForm
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'property_type', 'image', 'available', 'contact_number']
