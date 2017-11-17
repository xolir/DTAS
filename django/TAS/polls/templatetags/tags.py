
from django.contrib.auth import get_user_model
from django.template.defaultfilters import register


@register.simple_tag
def count_role_changes():
    User = get_user_model()
    users = User.objects.filter(request_role_change=True)
    count_role_changes = len(users)
    return count_role_changes