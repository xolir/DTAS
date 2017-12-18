from django.contrib.auth import get_user_model
from django.forms import DateField, ModelForm, MultipleChoiceField, SelectMultiple, TextInput, PasswordInput
from registration.forms import RegistrationForm

from django import forms

from TAS import settings
from polls.models import Question

User = get_user_model()

class MyCustomUserForm(RegistrationForm):
    birthday = DateField(label='', input_formats=settings.DATE_INPUT_FORMATS, widget=forms.TextInput(attrs={'placeholder': 'Birthday', 'required': True}))
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name', 'required': True}));
    surname = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Surname', 'required': True}));
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email', 'required': True}));
    password1 = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'required': True}));
    password2 = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation', 'required': True}));

    class Meta:
        model = get_user_model()
        fields = ('name', 'surname', 'birthday', 'email', 'password1', 'password2',)


class QuestionForm(ModelForm):
    myfield = MultipleChoiceField(choices=['a', 'b'], widget=SelectMultiple)

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date',)