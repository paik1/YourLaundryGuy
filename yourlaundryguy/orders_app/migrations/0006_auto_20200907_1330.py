# Generated by Django 3.0.7 on 2020-09-07 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders_app', '0005_auto_20200907_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
