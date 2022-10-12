# Generated by Django 3.2.9 on 2022-10-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20221012_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='desc',
        ),
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.URLField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]