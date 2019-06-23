from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CafeProfile, Category

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    birth_date = forms.DateField()
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'phone_number')


class ContactForm(forms.Form):
    first_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    phone_number = forms.CharField(label='', max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    email = forms.EmailField(label='', required=True, max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
    category = forms.ModelChoiceField(queryset=Category.objects.filter(used_for='Support'))
    subject = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    comments = forms.CharField(label='', required=True, max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Questions, '
                                                                                                       'comments, or '
                                                                                                       'concerns',
                                                                                                       'id' : 'comments',}))

