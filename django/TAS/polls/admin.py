from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from rolepermissions.roles import get_user_roles
from django.forms import CheckboxSelectMultiple

from polls.forms import QuestionForm
from .models import Question, Choice, Vote

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
    list_display = ('question_text', 'pub_date', 'was_published_recently',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Candidates', {'fields': ['user']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question_text']

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['user'].queryset = User.objects.filter(role='Candidate')
        return super(QuestionAdmin, self).render_change_form(request, context, args, kwargs)


class VotesAdmin(admin.ModelAdmin):
    actions = None
    list_display_links = None
    list_display = ('question_id', 'get_Name', 'votes')
    readonly_fields = ('votes', 'user_id', 'question_id')
    list_filter = ('question_id', )

    def get_Name(self, obj):
        userObj = User.objects.get(email=obj.user_id)
        name = userObj.name
        surname = userObj.surname
        return name + " " + surname
    get_Name.short_description = "Name"

    fieldsets = [
        (None, {'fields': ()}),
    ]


class VotesAdmin(admin.ModelAdmin):
    actions = None
    list_display_links = None
    list_display = ('question_id', 'get_Name', 'votes')
    readonly_fields = ('votes', 'user_id', 'question_id')
    list_filter = ('question_id', )

    def get_Name(self, obj):
        userObj = User.objects.get(email=obj.user_id)
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
