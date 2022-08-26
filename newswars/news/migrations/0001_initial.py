# Generated by Django 2.2 on 2022-08-26 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=1000)),
                ('img', models.URLField(max_length=1000)),
                ('link', models.URLField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Channel')),
            ],
        ),
    ]
