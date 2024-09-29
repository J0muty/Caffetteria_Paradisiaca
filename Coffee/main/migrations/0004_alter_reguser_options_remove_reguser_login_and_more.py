# Generated by Django 5.1 on 2024-09-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0003_reguser_delete_reguser1_delete_reguser2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reguser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='reguser',
            name='login',
        ),
        migrations.AddField(
            model_name='reguser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='reguser_set', to='auth.group'),
        ),
        migrations.AddField(
            model_name='reguser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reguser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reguser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='reguser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='reguser_set', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
