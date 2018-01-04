import datetime
from django.core.mail import send_mail
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import BaseUserManager
from rolepermissions.roles import assign_role
from TAS import settings


class Question(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('ending date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def has_ended(self):
        now = timezone.now()
        return self.end_date <= now
    has_ended.admin_order_field = 'end_date'
    has_ended.boolean = True
    has_ended.short_description = 'Has ended?'

    def sorted_votes(self):
        return sorted(self.vote_set.all(), key=lambda vote: vote.votes, reverse=True)
    
    def current_leader(self):
        try:
            return self.sorted_votes()[0].user_id
        except:
            return None

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
    request_role_change = models.BooleanField(
        _('role change'),
        default=False,
        help_text=_('Designates whether the user has requested role change'),
    )
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
            return self.name + " " + self.surname

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


class Vote(models.Model):
    votes = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='poll')


class Elector(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='poll')
    has_voted = models.BooleanField(default=False)


def set_role(sender, instance, created, **kwargs):
    if created:
        assign_role(instance, 'voter')
        instance.role = 'Voter'
        instance.save()


def add_candidate_to_vote_table(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        users = instance.user.all()
        for u in users:
            try:
                vote = Vote.objects.get(user_id=u.id, question_id=instance.id)
                continue
            except Vote.DoesNotExist:
                try:
                    latestObj = Vote.objects.latest('id')
                    vote = Vote(latestObj.id + 1, 0, u.id, instance.id)
                    vote.save()
                except Vote.DoesNotExist:
                    vote = Vote(1, 0, u.id, instance.id)
                    vote.save()
    if action == 'pre_remove':
        for i in pk_set:
            vote = Vote.objects.get(user_id=i, question_id=instance.id)
            vote.delete()


m2m_changed.connect(add_candidate_to_vote_table, sender=Question.user.through)
post_save.connect(set_role, sender=settings.AUTH_USER_MODEL)