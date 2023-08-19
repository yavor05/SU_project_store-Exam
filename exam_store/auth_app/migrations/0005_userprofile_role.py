# Generated by Django 4.2.3 on 2023-08-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('staff', 'Staff'), ('user', 'User'), ('admin', 'Admin')], default='user', max_length=10),
        ),
    ]