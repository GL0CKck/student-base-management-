import datetime


from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Student


@receiver(post_save, sender=Student)
def signal_create_user(sender, instance, created, pub_date=datetime.datetime.now(), **kwargs):
    if created:
        user = Student.object.get(id=instance.id)
        print(f'Create new student {pub_date} - {user}')


@receiver(post_delete, sender=Student)
def signal_delete_user(sender, instance, pub_date=datetime.datetime.now(), **kwargs):
    print(f'User delete {pub_date} - {instance.email}')

