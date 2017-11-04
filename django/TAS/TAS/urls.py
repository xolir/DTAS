"""TAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from registration.backends.hmac.views import RegistrationView
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
from polls import views
from polls.forms import MyCustomUserForm


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


api_urlpatterns = [
    url(r'accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register',
    ),
    url(r'^accounts/password/reset/auth_password_reset_done$',
        auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^accounts/password/reset/confirm/NA/set-password/auth_password_reset_complete$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^accounts/password/change$',
        auth_views.password_change,
        name='password_change'),
    url(r'^accounts/password/change/auth_password_change_done$',
        auth_views.password_change_done,
        name='password_change_done'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(api_urlpatterns)),
]