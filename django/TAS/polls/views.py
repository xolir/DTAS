from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from rest_framework import viewsets

from polls.serializers import UserSerializer, QuestionSerializer, VoteSerializer
from .models import Question, Vote, Elector


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        Makes sure that users won't guess the url.
        """
        return Question.objects.filter(pub_date__lte=timezone.now(),
                                       end_date__gte=timezone.now())


class FinishedPollsView(generic.ListView):
    model = Question
    template_name = 'polls/finishedpolls.html'
    context_object_name = 'finished_polls_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now(), end_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    User = get_user_model()
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.user.get(pk=request.POST['user'])
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a candidate.",
        })
    else:
        try:
            elector = Elector.objects.get(user_id=request.user.id, question_id=question_id, has_voted=True)
            return render(request, 'polls/detail.html',{
                'question': question,
                'error_message': 'You have already voted',
            })
        except Elector.DoesNotExist:
            try:
                latestElector = Elector.objects.latest('id')
                elector = Elector(latestElector.id + 1, request.user.id, question_id, True)
                elector.save()
                try:
                    vote = Vote.objects.get(user_id=selected_choice.id, question_id=question_id)
                    vote.votes += 1
                    vote.save()
                except Vote.DoesNotExist:
                    latestObj = Vote.objects.latest('id')
                    vote = Vote(latestObj.id + 1, 1, selected_choice.id, question.id)
                    vote.save()
            except Elector.DoesNotExist:
                elector = Elector(1, request.user.id, question_id, True)
                elector.save()
                try:
                    vote = Vote.objects.get(user_id=selected_choice.id, question_id=question_id)
                    vote.votes += 1
                    vote.save()
                except Vote.DoesNotExist:
                    latestObj = Vote.objects.latest('id')
                    vote = Vote(latestObj.id + 1, 1, selected_choice.id, question.id)
                    vote.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


############### REST API ##################
class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all().order_by('-surname')
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all().order_by('-question_id')
    serializer_class = VoteSerializer


