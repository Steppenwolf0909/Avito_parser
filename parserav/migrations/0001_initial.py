# Generated by Django 3.1.3 on 2021-05-05 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0)),
                ('telephone', models.CharField(max_length=15)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]