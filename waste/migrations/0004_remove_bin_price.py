# Generated by Django 4.2.5 on 2023-10-29 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0003_bin_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bin',
            name='price',
        ),
    ]
