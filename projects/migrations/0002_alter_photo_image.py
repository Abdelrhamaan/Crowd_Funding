# Generated by Django 4.2.2 on 2023-06-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
