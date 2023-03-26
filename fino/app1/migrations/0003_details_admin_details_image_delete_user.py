# Generated by Django 4.1.7 on 2023-03-23 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_remove_transactions_status_remove_user_is_currbal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='details',
            name='image',
            field=models.ImageField(default='adminp.jpg', upload_to='Profile_Images'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]