# Generated by Django 3.1.7 on 2021-03-25 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210325_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='house_no',
        ),
    ]
