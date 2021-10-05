from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Group(models.Model):
    title = models.CharField(unique=True, max_length=122, verbose_name='Название группы')
    super_group = models.ForeignKey('SuperGroup', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Группа')


class SuperGroupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_group__isnull=True)


class SuperGroup(Group):
    objects = SuperGroupManager()

    def __str__(self):
        return self.title

    class Meta:
        proxy = True
        ordering = ('title', )
        verbose_name = ' Над группа'
        verbose_name_plural = 'Над группы'


class SubGroupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_group__isnull=False)


class SubGroup(Group):
    objects = SuperGroupManager()

    def __str__(self):
        return f'{self.super_group.name} - {self.title}'

    class Meta:
        proxy = True
        ordering = ('super_group__name', 'title')
        verbose_name = 'Под группа'
        verbose_name_plural = 'Под группы'




