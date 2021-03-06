# Generated by Django 2.1.dev20171216185936 on 2018-01-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0004_deliveryaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
