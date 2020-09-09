# Generated by Django 3.0.7 on 2020-09-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0007_auto_20200907_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='status',
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]