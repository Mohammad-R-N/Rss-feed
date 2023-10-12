from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from podcasts.models import Channel
from core.models import BaseModel
from core.utils import phone_regex_validator
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import CustomUserManager


class Account(AbstractUser,PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(max_length=30, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=30, verbose_name=_('Last Name'))
    username = models.CharField(max_length=100,verbose_name=_("User Name"))
    email = models.EmailField(unique=True,verbose_name=_("Email"))
    password = models.CharField(max_length=18,verbose_name=_("Password"))
    phone_number = models.CharField(max_length=13, unique=True, validators=[phone_regex_validator],verbose_name=_('Phone Number'))
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True, editable=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name=_('Activation Status'))

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']

    def __str__(self) -> str:
        return self.username
   
    def save(self, *args, **kwargs):
        self.phone_number = '0' + self.phone_number[3:] if len(self.phone_number) == 13 else self.phone_number
        super(Account, self).save(*args, **kwargs)

    def role(self):
        return "Super User" if self.is_superuser else self.groups.get()

    role.short_description = _('Role')




class Notification(BaseModel):
    
    CHOICES = (
        ('l', 'login'),
        ('r', 'registery'),
        ('t', 'token'),
        ('o', 'others')
    )

    title = models.CharField(choices=CHOICES, max_length=1)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message