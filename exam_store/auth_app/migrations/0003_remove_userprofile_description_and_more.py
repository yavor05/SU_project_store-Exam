# Generated by Django 4.2.3 on 2023-08-17 15:19

import django.core.validators
from django.db import migrations, models
import exam_store.auth_app.validators
import exam_store.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_userprofile_age_alter_userprofile_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, default='None', max_length=40, null=True, validators=[django.core.validators.MinLengthValidator(2), exam_store.main.validators.validate_starts_with_uppercase, exam_store.auth_app.validators.letters_only_validator]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, default='None', max_length=40, null=True, validators=[django.core.validators.MinLengthValidator(2), exam_store.main.validators.validate_starts_with_uppercase, exam_store.auth_app.validators.letters_only_validator]),
        ),
    ]