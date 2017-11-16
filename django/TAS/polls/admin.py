from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from rolepermissions.roles import get_user_roles
from django.forms import CheckboxSelectMultiple

from polls.forms import QuestionForm
from .models import Question, Choice, Vote, Elector

User = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'birthday', 'is_staff', 'get_role', 'show_questions',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def get_role(self, instance):
        return instance.role
    get_role.short_description = 'Role'

    def show_questions(self, obj):
        return "<br>".join([a.question_text for a in obj.question_set.all()])
    show_questions.short_description = 'Questions'
    show_questions.allow_tags = True


# class ChoiceInline(admin.TabularInline):
#     model = User
#     fields = ('name', 'surname', )
#     readonly_fields = ('name', 'surname')
#     can_delete = False
#     extra = 0


class QuestionAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('question_text', 'pub_date', 'end_date', 'was_published_recently', 'has_ended', )
=======
    list_display = ('question_text', 'pub_date', 'end_date', 'was_published_recently', 'has_ended',)
>>>>>>> ee9c0a5269385d2e31cab2d903a0941a0b94bb5b
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date', 'end_date']}),
        ('Candidates', {'fields': ['user']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question_text']

    # def getNames(self,obj):
    #     list_candidates  = User.objects.filter(role='Candidate')
    #     list_candidates = [i.name + " " + i.surname for i in list_candidates]
    #     return list_candidates

    def render_change_form(self, request, context, *args, **kwargs):
        list_candidates = User.objects.filter(role='Candidate')
        #list_candidates = [i.name for i in list_candidates]
        context['adminform'].form.fields['user'].queryset = list_candidates
        return super(QuestionAdmin, self).render_change_form(request, context, args, kwargs)


class VotesAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ('question_id', 'get_Name', 'user_id', 'votes')
    readonly_fields = ('votes', 'user_id', 'question_id')
    list_filter = ('question_id', 'user_id', )

    def get_Name(self, obj):
        userObj = User.objects.get(email=obj.user_id)
        name = userObj.name
        surname = userObj.surname
        return name + " " + surname
    get_Name.short_description = "Name"

    fieldsets = [
        (None, {'fields': ()}),
    ]


class ElectorAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ('question', 'get_Name', 'user', 'has_voted')
    readonly_fields = ('question', 'user', 'has_voted')
    list_filter =('question', 'user', )

    def get_Name(self, obj):
        userObj = User.objects.get(email=obj.user)
        name = userObj.name
        surname = userObj.surname
        return name + " " + surname
    get_Name.short_description = "Name"

    fieldsets = [
        (None, {'fields': ()}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Vote, VotesAdmin)
admin.site.register(Elector, ElectorAdmin)
