# Generated by Django 3.2.9 on 2022-10-05 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='color',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='logo',
        ),
    ]