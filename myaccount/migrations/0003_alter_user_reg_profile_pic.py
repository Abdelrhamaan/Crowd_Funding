# Generated by Django 4.2.2 on 2023-06-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0002_alter_user_reg_activated_alter_user_reg_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='profile_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
