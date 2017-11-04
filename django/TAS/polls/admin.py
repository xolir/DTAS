from django.contrib import admin
from django.contrib.auth import get_user_model
from rolepermissions.roles import get_user_roles

from .models import Question, Choice



User = get_user_model()




class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'birthday', 'is_staff', 'get_role')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def get_role(self, instance):
        return get_user_roles(instance)
    get_role.short_description = 'Role'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, CustomUserAdmin)
