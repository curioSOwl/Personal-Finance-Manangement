# Generated by Django 4.1.7 on 2023-03-24 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_details_admin_details_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='dail_el',
        ),
    ]