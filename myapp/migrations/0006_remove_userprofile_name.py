# Generated by Django 5.0.4 on 2024-05-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
