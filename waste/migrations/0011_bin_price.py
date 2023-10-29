# Generated by Django 4.2.5 on 2023-10-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0010_remove_bin_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Calculated price based on load type', max_digits=8),
        ),
    ]