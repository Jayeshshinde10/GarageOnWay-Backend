# Generated by Django 5.0.1 on 2024-02-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_customer_latitude_customer_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='latitude',
            field=models.FloatField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='longitude',
            field=models.FloatField(max_length=30),
        ),
    ]
