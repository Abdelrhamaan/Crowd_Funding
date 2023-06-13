# Generated by Django 4.2.2 on 2023-06-11 12:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0005_alter_user_reg_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='phone_num',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format '01X XXX XXXX', where X is a digit.", regex='^01[0-2]{1}[0-9]{8}$')]),
        ),
    ]
