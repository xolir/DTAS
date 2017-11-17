from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^finishedpolls$', views.FinishedPollsView.as_view(), name='finishedpolls'),
    url(r'^requestrole$', views.change_role, name='requestrole'),
    url(r'^rolechange$', views.ChangeRoleView.as_view(), name='changerole'),
    url(r'^rolechange_save', views.save_role_change, name='rolechange_save')
]