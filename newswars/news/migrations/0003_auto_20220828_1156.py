# Generated by Django 3.2.9 on 2022-08-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220826_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]