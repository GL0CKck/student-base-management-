# Generated by Django 3.2.8 on 2022-02-08 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220208_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='students',
        ),
        migrations.DeleteModel(
            name='StudentGroupRelation',
        ),
    ]
