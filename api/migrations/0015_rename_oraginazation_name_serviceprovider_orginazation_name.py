# Generated by Django 5.0.1 on 2024-03-04 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_serviceprovider_image1_serviceprovider_image2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='oraginazation_name',
            new_name='orginazation_name',
        ),
    ]