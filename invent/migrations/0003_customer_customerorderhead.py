# Generated by Django 2.1.dev20171216185936 on 2018-01-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0002_auto_20180104_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vat_no', models.CharField(max_length=30, null=True)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('phone1', models.CharField(max_length=10, null=True)),
                ('phone2', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField()),
                ('stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrderHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
