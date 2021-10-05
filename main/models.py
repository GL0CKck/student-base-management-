from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Group(models.Model):
    title = models.CharField(unique=True, max_length=12, verbose_name='Название группы')
    super_group = models.ForeignKey()


class SuperGroupManager(models.Manager):
    pass


