# Generated by Django 5.1 on 2024-09-24 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reguser2',
            name='user',
        ),
    ]
