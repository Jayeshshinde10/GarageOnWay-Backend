# Generated by Django 5.0.1 on 2024-01-16 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oraginazation_name', models.CharField(max_length=50)),
                ('closing_time', models.TimeField()),
                ('opening_time', models.TimeField()),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('serviceProvider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.serviceprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_Approved', models.BooleanField(default=False)),
                ('is_Completed', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('Service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
                ('ServiceProvider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.serviceprovider')),
            ],
        ),
    ]