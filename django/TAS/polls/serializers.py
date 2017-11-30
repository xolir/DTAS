from django.contrib.auth import get_user_model
from rest_framework import serializers

from polls.models import Question, Vote


class UserSerializer(serializers.HyperlinkedModelSerializer):
    User = get_user_model()
    class Meta:
        model = get_user_model()
        fields = ('id', 'url', 'email', 'name', 'surname', 'role', 'birthday')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'user', 'pub_date', 'end_date')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('question_id', 'user_id', 'votes')

