# Generated by Django 3.0.7 on 2020-06-10 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='phone number')),
                ('name', models.CharField(max_length=150, null=True)),
                ('roll', models.CharField(max_length=20, unique=True, verbose_name='roll')),
                ('date_joind', models.DateTimeField(auto_now_add=True, verbose_name='date joind')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]