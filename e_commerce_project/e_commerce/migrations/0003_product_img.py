# Generated by Django 5.1.3 on 2025-01-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0002_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
