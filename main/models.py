from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Group(models.Model):
    name = models.CharField(db_index=True, unique=True, max_length=122,
                            verbose_name='Название группы')
    is_headman = models.ForeignKey('Student', on_delete=models.PROTECT,
                                   null=True,
                                   blank=True,
                                   verbose_name='Староста',
                                   related_name='headman')
    super_group = models.ForeignKey('SuperGroup', on_delete=models.PROTECT,
                                    null=True,
                                    blank=True,
                                    verbose_name='Группа')


class SuperGroupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_group__isnull=True)


class SuperGroup(Group):
    objects = SuperGroupManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('name', )
        verbose_name = 'Над группа'
        verbose_name_plural = 'Над группы'


class SubGroupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_group__isnull=False)


class SubGroup(Group):
    objects = SubGroupManager()

    def __str__(self):
        return f'{self.super_group.name} - {self.name}'

    class Meta:
        proxy = True
        ordering = ('super_group__name', 'name')
        verbose_name = 'Под группа'
        verbose_name_plural = 'Под группы'


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Не найденно студенто с таким email!')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be True')

        return self._create_user(email, password, **extra_fields)


class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=19, verbose_name='Имя')
    last_name = models.CharField(max_length=29, verbose_name='Фамилия')
    group = models.ForeignKey(SubGroup, on_delete=models.CASCADE, related_name='supergroup', blank=True, null=True)
    data_joined = models.DateField(auto_now_add=True, db_index=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('last_name', )
    object = UserManager()

    def get_full_name(self):
        full_name = f'{self.first_name} + {self.last_name}'
        return full_name

    def get_short_name(self):
        return self.last_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'






