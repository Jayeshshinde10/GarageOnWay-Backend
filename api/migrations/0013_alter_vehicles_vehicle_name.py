# Generated by Django 5.0.1 on 2024-03-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_vehicles_order_vehicle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='vehicle_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]