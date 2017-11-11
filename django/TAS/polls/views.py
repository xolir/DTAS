from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question, Vote


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        Makes sure that users won't guess the url.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


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
            vote = Vote.objects.get(user_id=selected_choice.id, question_id=question_id)
            vote.votes += 1
            vote.save()
        except Vote.DoesNotExist:
            latestObj = Vote.objects.latest('id')
            vote = Vote(latestObj.id + 1, 1, selected_choice.id, question.id)
            vote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

