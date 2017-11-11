# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
#
# from TAS import settings
#
#
# class SignUpForm(UserCreationForm):
#     birth_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, help_text='Required. Format: dd-mm-yyyy')
#
#     class Meta:
#         User = get_user_model()
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'birth_date', 'username', 'password1', 'password2', )
from django.contrib.auth import get_user_model
from django.forms import DateField, ModelForm, MultipleChoiceField, SelectMultiple
from registration.forms import RegistrationForm

from TAS import settings
from polls.models import Question

User = get_user_model()

class MyCustomUserForm(RegistrationForm):
    birthday = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = get_user_model()
        fields = ('name', 'surname', 'birthday', 'email', 'password1', 'password2',)


class QuestionForm(ModelForm):
    myfield = MultipleChoiceField(choices=['a', 'b'], widget=SelectMultiple)

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date',)