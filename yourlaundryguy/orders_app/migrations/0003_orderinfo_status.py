# Generated by Django 3.0.7 on 2020-09-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0002_orderinfo_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(choices=[('P', 'placed'), ('C', 'collected'), ('D', 'delievered'), ('X', 'cancelled')], default='P', max_length=1),
        ),
    ]
