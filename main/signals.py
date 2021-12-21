from django.dispatch import receiver
import django.dispatch
from django.db.models.signals import pre_save, post_delete
from .models import Student
import datetime


@receiver(pre_save, sender=Student)
def my_handler(sender, pub_date=datetime.datetime.now(), **kwargs):
    print(f'Create new student {pub_date}')


@receiver(post_delete, sender=Student)
def signal_delete_user(sender, pub_date=datetime.datetime.now(), **kwargs):
    print(f'User delete {pub_date}')