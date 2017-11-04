import datetime

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager
from rolepermissions.roles import assign_role


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        assign_role(user, 'doctor')
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    role = models.CharField(max_length=50, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, *args, **kwargs):
        send_mail(
            '{}'.format(args[0]),
            '{}'.format(args[1]),
            '{}'.format(args[2]),
            [self.email],
            fail_silently=False,
        )

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# class Profile(models.Model):
#     CANDIDATE = 1
#     VOTER = 2
#     ROLE_CHOICES =(
#         (CANDIDATE, 'Candidate'),
#         (VOTER, 'Voter')
#     )
#     birthday = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
#     votes = models.IntegerField(default=0)
#     accepted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Candidate(models.Model):
#     polls = models.ManyToManyField(Question)
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     birthday = models.DateField(auto_now=False, auto_now_add=False)
#     email = models.EmailField(max_length=254)
#     votes = models.IntegerField(default=0)
#     accepted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name + " " + self.surname
#
#
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
#
#
# class Voter(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     birthday = models.DateField(auto_now=False, auto_now_add=False)
#     email = models.EmailField(max_length=254)
#     hasVoted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name + " " + self.surname




