# Generated by Django 5.1.3 on 2025-02-21 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0005_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
