# Generated by Django 5.0.2 on 2024-05-07 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0002_alter_commission_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobapplication',
            options={'verbose_name': 'applicant', 'verbose_name_plural': 'applicants'},
        ),
    ]
