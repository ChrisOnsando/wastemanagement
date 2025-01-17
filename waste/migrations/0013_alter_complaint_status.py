# Generated by Django 4.2.5 on 2023-10-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0012_alter_bin_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('inprogress', 'InProgress'), ('approved', 'Approved')], default='p', help_text='Status', max_length=10),
        ),
    ]
