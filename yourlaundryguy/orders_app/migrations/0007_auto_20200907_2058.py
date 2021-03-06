# Generated by Django 3.0.7 on 2020-09-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0006_auto_20200907_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(choices=[('P', 'Placed'), ('C', 'Collected'), ('D', 'Delievered'), ('X', 'Cancelled')], default='P', max_length=5),
        ),
    ]
