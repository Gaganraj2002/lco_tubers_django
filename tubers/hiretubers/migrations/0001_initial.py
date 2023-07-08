# Generated by Django 4.2.3 on 2023-07-08 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiretuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('tuber_id', models.IntegerField()),
                ('tuber_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
