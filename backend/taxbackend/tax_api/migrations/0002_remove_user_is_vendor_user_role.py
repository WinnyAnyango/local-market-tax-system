# Generated by Django 5.2.1 on 2025-06-10 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_vendor',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Super Admin'), ('admin', 'Admin'), ('vendor', 'Vendor')], default='vendor', max_length=20),
        ),
    ]
