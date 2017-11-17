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