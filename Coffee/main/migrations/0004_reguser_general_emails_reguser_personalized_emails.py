# Generated by Django 5.1.1 on 2024-10-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_reguser_dark_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='general_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reguser',
            name='personalized_emails',
            field=models.BooleanField(default=False),
        ),
    ]