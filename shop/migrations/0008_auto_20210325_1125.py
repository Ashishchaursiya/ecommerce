# Generated by Django 3.1.7 on 2021-03-25 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_returnable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]
