# Generated by Django 5.0.1 on 2024-02-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customer_latitude_alter_customer_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]