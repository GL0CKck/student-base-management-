# Generated by Django 3.2.8 on 2022-03-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220208_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_request',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последний запрос'),
        ),
    ]