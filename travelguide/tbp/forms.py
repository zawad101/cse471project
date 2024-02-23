from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class TravelerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    name = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])


    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'age', 'name', 'gender', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.age = self.cleaned_data['age']
        user.name = self.cleaned_data['name']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user
    
class TravelerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

# forms.py
from django import forms
from .models import traveler

class TravelerUpdateForm(forms.ModelForm):
    class Meta:
        model = traveler
        fields = ['email', 'phone', 'age', 'name', 'gender']

