# Generated by Django 4.1.7 on 2023-03-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_transactions_curbal_transactions_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
