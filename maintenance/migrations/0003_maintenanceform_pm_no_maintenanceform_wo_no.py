# Generated by Django 4.2.1 on 2023-05-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_maintenanceform_unit_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenanceform',
            name='pm_No',
            field=models.CharField(blank=True, default='1407', max_length=7, null=True, verbose_name='PM No.'),
        ),
        migrations.AddField(
            model_name='maintenanceform',
            name='wo_No',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='WO No.'),
        ),
    ]
