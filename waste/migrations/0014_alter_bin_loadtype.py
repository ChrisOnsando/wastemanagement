# Generated by Django 4.2.5 on 2023-10-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0013_alter_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='loadtype',
            field=models.CharField(blank=True, choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='l', help_text='Type of Load', max_length=10),
        ),
    ]
