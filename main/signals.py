from django.dispatch import receiver
import django.dispatch
from django.db.models.signals import pre_save, post_delete, post_save
from .models import Student
import datetime


@receiver(post_save, sender=Student)
def signal_delete_user(sender, instance, created, pub_date=datetime.datetime.now(), **kwargs):
    if created:
        user = Student.object.get(id=instance.id)
        print(f'Create new student {pub_date} - {user}')


@receiver(post_delete, sender=Student)
def signal_delete_user(sender, pub_date=datetime.datetime.now(), **kwargs):
    print(f'User delete {pub_date} ')

